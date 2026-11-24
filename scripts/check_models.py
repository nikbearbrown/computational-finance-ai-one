"""Offline synthetic finance checks. Python 3. Standard library only."""
from fractions import Fraction as Q
from math import prod, sqrt
from pathlib import Path
import json

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic-labs.json"


def amount(x):
    if isinstance(x, bool) or not isinstance(x, (int, str, Q)):
        raise ValueError("supply a declared number or exact decimal string")
    return Q(x)


def pv(ledger, rate):
    """Discount unique explicitly dated cash flows. Aggregate same-date rows first."""
    g = 1 + amount(rate)
    if g <= 0:
        raise ValueError("invalid effective rate")
    if not ledger:
        raise ValueError("no cash flows")
    seen = set()
    value = Q()
    for year, cash in ledger:
        if type(year) is not int or year < 0 or year in seen:
            raise ValueError("unique nonnegative integer periods required")
        seen.add(year)
        value += amount(cash) / g**year
    return value


def period_return(start, end, distribution):
    a,b,c = map(amount,(start,end,distribution))
    if a<=0 or b<0 or c<0:
        raise ValueError("positive start price and nonnegative end price and distribution required")
    return (b+c)/a-1


def drawdowns(wealth):
    values = [amount(v) for v in wealth]
    if not values or min(values)<=0:
        raise ValueError("nonempty positive wealth path required for this exercise")
    peak = values[0]
    result = []
    for v in values:
        peak = max(v,peak)
        result.append(v/peak-1)
    return result


def call_replicate(spot, up, down, strike, gross):
    s,u,d,k,g = map(amount,(spot,up,down,strike,gross))
    if g<=0 or not 0<=d<s*g<u or k<0:
        raise ValueError("unsupported tree or out-of-range pricing weight")
    a,b=max(u-k,0),max(d-k,0)
    delta=(a-b)/(u-d)
    cash=(b-d*delta)/g
    price=s*delta+cash
    probability=(s*g-d)/(u-d)
    return price, delta, cash, probability


def covariance(a,b):
    if len(a)!=len(b) or len(a)<2:
        raise ValueError("need at least two same-period pairs")
    a,b=[amount(x) for x in a],[amount(y) for y in b]
    aa,bb=sum(a)/len(a),sum(b)/len(b)
    return sum((x-aa)*(y-bb) for x,y in zip(a,b))/(len(a)-1)


def scenario_variance(weight_b, vol_a, vol_b, correlation):
    b,x,y,r=map(amount,(weight_b,vol_a,vol_b,correlation))
    if not 0<=b<=1 or min(x,y)<0 or not -1<=r<=1:
        raise ValueError("invalid weight, volatility or correlation")
    a=1-b
    return a*a*x*x+b*b*y*y+2*a*b*x*y*r


def evaluate_packet(d, counts, bond_price=None, low=None):
    n_bond,n_equity=counts
    if min(n_bond,n_equity)<0 or any(type(v) is not int for v in counts):
        raise ValueError("nonnegative integer units required")
    bond=amount(d["bond_unit_cost"] if bond_price is None else bond_price)
    cost=n_bond*bond+n_equity*amount(d["equity_unit_cost"])
    payoff=n_bond*amount(d["bond_terminal_cash"])
    high=payoff+n_equity*amount(d["equity_high"])
    low=payoff+n_equity*amount(d["equity_low"] if low is None else low)
    return cost,high,low,(high+low)/2,cost==d["capital"],min(high,low)>=d["floor"]


def verify(inputs):
    n = 0

    def check(actual, expected):
        nonlocal n
        if actual != expected:
            raise AssertionError((n+1,actual,expected))
        n += 1

    def rounded(val, expected, digits=2):
        check(round(val,digits),Q(expected))

    def rejected(f):
        nonlocal n
        try:
            f()
        except (ValueError, ZeroDivisionError, TypeError):
            n += 1
        else:
            raise AssertionError("invalid input accepted")

    # Ch 1: an observed price agreement is not a timing check.
    zero=inputs["zero"]
    zero_ledger=[(zero["terminal_year"],zero["amount"])]
    rate=Q(zero["annual_rate"])
    base=pv(zero_ledger,rate)
    check(base,100)
    check(base*(1+rate),105)
    check(pv(zero_ledger,0),105)
    rounded(pv(zero_ledger,".10"),"95.45")
    rounded(pv([(2,105)],rate),"95.24")
    check(pv(zero_ledger,0)>base>pv(zero_ledger,".10"),True)
    rejected(lambda:pv([(1,100),(1,5)],rate))
    rejected(lambda:pv([(1,None)],rate))
    rejected(lambda:pv([(True,105)],rate))
    rejected(lambda:pv(zero_ledger,-1))

    # Ch 2: returns, independent path, sample fluctuation.
    rows=inputs["monthly"]["rows_start_end_distribution"]
    rr=[period_return(*row) for row in rows]
    check(rr,[Q(".05"),Q(-8,103)])
    factor=prod(1+r for r in rr)
    check(factor,Q("1.05")*95/103)
    rounded((factor-1)*100,"-3.16")
    rounded((factor**6-1)*100,"-17.50")
    check(rows[-1][1]+rows[0][2],97)
    rejected(lambda:period_return(100,103,None))
    rejected(lambda:period_return(0,103,2))
    path=inputs["wealth"]
    dd=drawdowns(path)
    check((dd[2],min(dd),dd[-1]),(Q("-.10"),Q("-.20"),Q("-.16")))
    dd2=drawdowns(path[:-1]+["91.96"])
    check((min(dd2),dd2[-1]),(Q("-.24"),Q("-.24")))
    rejected(lambda:drawdowns([]))
    toy=[(Q(a)+Q(b))/2 for a in ("-.10",".10") for b in ("-.10",".10")]
    check(toy,[Q("-.10"),0,0,Q(".10")])
    check(sum(t*t for t in toy)/4,Q(".005"))
    check(round(sqrt(.005)*100,2),7.07)

    # Ch 3: check securities on their own rates.
    b=inputs["coupon_bond"]
    bond=pv(b["receipts"],b["annual_yield"])
    par=pv(b["receipts"],".06")
    rounded(bond,"101.86")
    check(par,100)
    weighted=pv([(1,6),(2,212)],b["annual_yield"])
    dur=weighted/bond
    rounded(dur,"1.9439",4)
    rounded(dur/(1+Q(b["annual_yield"])),"1.8513",4)
    rounded((par/bond-1)*100,"-1.83")
    check(pv([(2,200)],".05")/pv([(2,100)],".05"),2)
    rounded(Q("2.8")/(Q(".09")-Q(".035")),"50.91")

    # Ch 4: exposure and return conventions.
    nav=[Q(a) for a in inputs["fund"]["nav"]]
    price=[Q(a) for a in inputs["fund"]["price"]]
    rounded((price[0]/nav[0]-1)*100,".60")
    rounded((price[1]/nav[1]-1)*100,"-.60")
    rounded((nav[1]/nav[0]-1)*100,".20")
    rounded((price[1]/price[0]-1)*100,"-.99")
    rounded((nav[1]/price[0]-1)*100,"-.40")
    gross=Q(".75")*Q(".016")+Q(".25")*Q(".002")
    check((gross,gross-Q(".001")),(Q(".0125"),Q(".0115")))

    # Ch 5: equal totals can coexist with different timing.
    o=inputs["operation"]
    val=pv(o["receipts"],o["annual_rate"])
    rounded(val,"3.51")
    check(pv(o["receipts"],0),20)
    late=pv([(t+1,x) for t,x in o["receipts"]],o["annual_rate"])
    check(late,val/(1+Q(o["annual_rate"])))
    rounded(pv(o["receipts"][:-1]+[(4,45)],o["annual_rate"]),".86")

    # Ch 6: leverage and fixed claim versus restricted proceeds.
    m=inputs["margin"]
    dd=m["loan"]; maintenance=Q(m["maintenance"])
    initial=m["start_asset"]-dd
    ratios=[Q(a-dd,a) for a in m["asset_levels"]]
    check([a>=maintenance for a in ratios],[True,False])
    rounded((Q(m["asset_levels"][0]-dd,initial)-1)*100,"-41.67")
    rounded(100*ratios[0],"46.67")
    rounded(100*ratios[1],"38.46")
    rounded(dd/(1-maintenance),"666.67")
    check((700-10*62,(700-10*62)-200),(80,-120))
    a=m["asset_levels"][1]
    dr=maintenance*a-(a-dd)
    collateral=dr/(1-maintenance)
    check((collateral,dr),(Q(50,3),10))
    check((a+collateral-dd)/(a+collateral),maintenance)
    check((a-(dd-dr))/a,maintenance)

    # Ch 7: replicate both states, and compare independently to weights.
    op=inputs["option"]
    s,u,d,k,g=[amount(op[key]) for key in ("spot","up","down","strike","gross")]
    for strike, expected, delta_expected in [(k,"11.90",Q(1,2)),(110,"5.95",Q(1,4))]:
        v,delta,c,p=call_replicate(s,u,d,strike,g)
        a,b=max(u-strike,0),max(d-strike,0)
        check((delta,p),(delta_expected,Q(5,8)))
        check((u*delta+g*c,d*delta+g*c),(a,b))
        check(v,(a*p+b*(1-p))/g)
        check(max(s-strike/g,0)<=v<=s,True)
        rounded(v,expected)
    rejected(lambda:call_replicate(s,u,d,k,"1.20"))
    rejected(lambda:call_replicate(s,u,u,k,g))

    # Ch 8: distinct direct series vs variance decomposition.
    pa=inputs["paired"]
    a,b=pa["A_pp"],pa["B_pp"]
    check(len(set(pa["row_ids"])),len(a))
    ca,cb,cov=covariance(a,a),covariance(b,b),covariance(a,b)
    check((ca,cb,cov),(Q(232,3),Q(160,3),Q(-16,3)))
    returns=[Q(x+y,2) for x,y in zip(a,b)]
    check(returns,[-1,-4,8,5])
    check(covariance(returns,returns),(ca+cb+2*cov)/4)
    check(covariance(returns,returns),30)
    check(covariance(a,b[::-1]),Q(16,3))
    check(covariance([Q(x+y,2) for x,y in zip(a,b[::-1])],[Q(x+y,2) for x,y in zip(a,b[::-1])]),Q(106,3))
    rejected(lambda:covariance(a,b[:-1]))

    # Ch 9–10: enumerate only permitted weights, preserve sampling conventions.
    h=inputs["portfolio"]
    means=list(map(Q,h["means"])); legs=h["standard_deviations"]
    lo,hi,minimum=map(Q,[h["min_B"],h["max_B"],h["min_mean"]])
    def all_candidates(corr,minimum):
        result=[]
        for b in map(Q,h["B_weights"]):
            mean=(1-b)*means[0]+b*means[1]
            var=scenario_variance(b,*legs,corr)
            result.append((b,mean,var,lo<=b<=hi and mean>=minimum))
        return result
    p0=all_candidates(h["correlations"][0],minimum)
    p1=all_candidates(h["correlations"][1],minimum)
    check([c[3] for c in p0],[False,True,True,False])
    check([c[1] for c in p0],[Q(".06"),Q(".07"),Q(".075"),Q(".08")])
    check([c[1] for c in p0],[c[1] for c in p1])
    best=min((c for c in p0 if c[3]),key=lambda c:c[2])
    check(best[:3],(Q(".40"),Q(".07"),Q(".008704")))
    check(p1[1][2],Q(".020224"))
    check(round(sqrt(p0[1][2])*100,2),9.33)
    check(round(sqrt(p0[2][2])*100,2),10.30)
    check(round(sqrt(p1[1][2])*100,2),14.22)
    check([c[0] for c in all_candidates(h["correlations"][0],Q(".075")) if c[3]],[Q(".50")])
    check((p0[2][2],p1[2][2]),(Q(".010600"),Q(".022600")))
    rejected(lambda:scenario_variance(".4",*legs,"1.01"))
    stress=Q(".60")*Q("-.14")+Q(".40")*Q("-.20")
    check(stress,Q("-.164"))
    a,b,c=Q(".70")*Q(".60"),Q(".70")*Q(".40"),Q(".30")
    check((a,b,c,a+b+c),(Q(".42"),Q(".28"),Q(".30"),1))
    check(Q(".70")*best[1]+c*Q(".03"),Q(".058"))
    check(Q(".70")*stress+c*Q(".03"),Q("-.1058"))
    check(round(.7*sqrt(best[2])*100,2),6.53)
    check((600*Q("1.20"),400*Q(".95")),(720,380))
    check(Q(".60")*1100-720,-60)
    check((Q(".60")*1095,Q(".40")*1095),(657,438))

    # Ch 11: estimated slope and annual modeled premium are not substituted.
    f=inputs["market_factor"]
    x,y=f["X_pp"],f["Y_pp"]
    slope=covariance(x,y)/covariance(x,x)
    check(slope,Q("1.1"))
    check(sum(y)-slope*sum(x),0)
    check(sum((b-slope*a) for a,b in zip(x,y)),0)
    rf,mkt,beta=map(Q,[f["annual_riskfree"],f["annual_market_expected"],f["beta_scenario"]])
    premium=mkt-rf
    ret=rf+beta*premium
    check((ret,ret+Q(".5")*Q(".02")),(Q(".09"),Q(".10")))
    check([rf+b*premium for b in (Q(".8"),Q("1.4"))],[Q(".07"),Q(".10")])

    # Ch 12: independent data closure; an AR timing change leaves total assets unchanged.
    s=inputs["statements"]; o,c=s["opening"],s["closing"]
    check(o["cash"]+o["ar"]+o["inventory"]+o["ppe"],o["ap"]+o["equity"])
    ow=o["ar"]+o["inventory"]-o["ap"]
    cw=c["ar"]+c["inventory"]-c["ap"]
    check((ow,cw,cw-ow),(75,83,8))
    profit=(s["sales"]-s["opex"])*(1-Q(s["cash_tax"]))
    flow=profit+s["depreciation"]-s["capex"]-(cw-ow)
    cash=o["cash"]+flow-s["distribution"]
    ppe=o["ppe"]+s["capex"]-s["depreciation"]
    equity=o["equity"]+profit-s["distribution"]
    check((profit,flow,cash,ppe,equity),tuple(map(Q,("63.75","37.75","87.75","228","398.75"))))
    check(cash+c["ar"]+c["inventory"]+ppe,c["ap"]+equity)
    rounded(pv([(1,flow)],s["pricing_rate"]),"34.32")
    check((cash-10)+(c["ar"]+10)+c["inventory"]+ppe,c["ap"]+equity)
    rounded(pv([(1,flow-10)],s["pricing_rate"]),"25.23")

    # Ch 13: exact threshold, just below, and price mismatch are separate flags.
    a=inputs["assessment"]
    check(base,a["bond_unit_cost"])
    A,B=a["candidates"]["A"],a["candidates"]["B"]
    check(evaluate_packet(a,A),(1000,1150,970,1060,True,False))
    check(evaluate_packet(a,B),(1000,1100,1010,1055,True,True))
    check(evaluate_packet(a,A,low=70),(1000,1150,910,1030,True,False))
    check(evaluate_packet(a,B,low=70),(1000,1100,980,1040,True,True))
    check(evaluate_packet(a,B,low=69),(1000,1100,978,1039,True,False))
    check(evaluate_packet(a,B,bond_price=pv([(2,105)],rate))[-2:],(False,True))
    check(evaluate_packet(a,B,bond_price=pv(zero_ledger,".10"))[-2:],(False,True))
    rejected(lambda:evaluate_packet(a,[8,Q("2.1")]))
    rejected(lambda:evaluate_packet(a,[-1,11]))
    return n


if __name__ == "__main__":
    cases = json.loads(DATA.read_text(encoding="utf-8"))
    print(f"{verify(cases)} check assertions passed for the synthetic Computational Finance models and capstone.")

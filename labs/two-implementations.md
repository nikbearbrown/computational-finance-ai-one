# One Financial Model, Two Implementations

Use a calculator first for at least one result. Then choose Excel or Python for the same dated model. The worksheet recipes use ordinary cells, not macros or proprietary plugins. English-language Excel examples use a period for decimal values and comma argument separators; a localized Excel installation may require different separators. Formula output is illustrative until it is recalculated and checked in the learner's environment. Python cases have an offline checker based on exact rational arithmetic before display rounding.

If you use an agent, supply the stated assumptions and a narrow request: “Implement these two rows, report blank inputs, and leave a visible binding-state test.” Check its result. Do not hand it a brokerage account, a current quote or private file. Either tool can make a consistent and wrong model.

## 1. Dated present value, zero and a coupon bond

In a clean sheet, enter `A1=Year`, `B1=Cash`, `C1=PV`. In A2:A4 enter 0, 1, 2. In D1 enter `0.05` as a number or 5%. For the simple benchmark put 0, 105, 0 in B2:B4. In C2 enter `=IF(COUNT(A2:B2,$D$1)=3,B2/(1+$D$1)^A2,NA())` and fill down. Compare `=SUM(C2:C4)` with 100; at D1=10%, compare with 105/1.10. Confirm that A2:A4 are unique nonnegative integer dates and D1 is a rate greater than −1. The COUNT guard makes a blank or text cell show an error; it does not check those financial assumptions. For the coupon bond leave the dates in place and replace B2:B4 with 0, 6, 106. The price is about 101.86; `=SUMPRODUCT(A2:A4,C2:C4)/SUM(C2:C4)` gives about 1.9439 years. At 6% the bond prices at par. Use NPV for equally spaced future cash only; add the initial amount separately, as explained in the [Microsoft NPV documentation](https://support.microsoft.com/en-us/excel/functions/npv-function).

In Python call `pv([(0,0),(1,105),(2,0)], "0.05")` from the checker (or sum each discounted amount with a loop). Add dates and validate them before summing. Compare the result against multiplication back to the promised 105. That multiplication—not another model's claim—is the simple oracle. In the Chapter 5 DCF, compare `-90+NPV(8%, future_range)` with the explicit 0–3 ledger. Enter an actual zero, not a blank, for a period with no cash.

## 2. Total return, reinvestment and drawdown

For the two monthly returns, put starting and ending price in A2:B3 as the pairs (100,103), (103,95). Put end-of-period distributions in C2:C3, 2 and 0. In D2 use `=IF(AND(COUNT(A2:C2)=3,A2>0),(B2+C2)/A2-1,NA())` and fill down. Gross returns are E2:E3 = `=1+D2` filled down. Cumulative return is `=PRODUCT(E2:E3)-1`. On the matching horizon the annual equivalent is `=PRODUCT(E2:E3)^6-1`. Put actual dates alongside the cells. This formula does not prove observations are comparable; check the join date and distribution basis first. Try deleting a distribution value; the guard must not silently treat it as observed zero.

For the separate six-entry wealth sequence in A2:A7, start B2 with `=MAX($A$2:A2)` and fill down for peaks. In C2 use `=A2/B2-1` and fill down. The worst signed drawdown is `=MIN(C2:C7)`. For a complete report confirm nonempty positive values and an increasing time index. The Python `period_return` and `drawdowns` functions implement the same choices; independently check 96.80/121−1 by hand.

## 3. Option replication and two payoff tests

Enter current underlying, up, down, strike and gross funding factor in B2:B6 as 100, 120, 80, 100, 1.05. Compute up payoff in B7 with `=MAX(B3-B5,0)`, down payoff in B8 with `=MAX(B4-B5,0)`, holdings in B9 with `=(B7-B8)/(B3-B4)`, risk-free position in B10 with `=(B8-B9*B4)/B6`, and price in B11 with `=B9*B2+B10`. Use `=AND(B4<B2*B6,B2*B6<B3)` to guard the strict pricing-weight condition. Test `=B3*B9+B6*B10` and the same expression with B4 to verify both payoffs. For an independent weight derivation in B12 use `=(B2*B6-B4)/(B3-B4)` then compare `=(B12*B7+(1-B12)*B8)/B6` against the price. Display tolerance checks without rounding the input positions. In Python `call_replicate` independently checks both state payoffs and pricing-weight equivalence. Change only the strike to 110 and repeat; an invalid discount assumption should be flagged before interpreting the result as a price.

## 4. Pair observations, then apply portfolio constraints

Put A returns −8, −2, 6, 12 and B returns 6, −6, 10, −2 in B2:C5, with matched row IDs in column A. Work in percentage points throughout this sheet. Verify row IDs, counts and completeness before using `=COVARIANCE.S(B2:B5,C2:C5)`. In D2 put `=(B2+C2)/2`, fill down, and compare `=VAR.S(D2:D5)` with the covariance decomposition in Chapter 8. For the illustrative Chapter 9 choice, switch to decimal returns in a different sheet. Put one candidate B weight in each row; compute A as 1−B, expected return as the weighted sum, and variance with individual standard deviations and a stated correlation. Write a feasibility flag for B between .20 and .50 and mean at least .07, using exact modeled input values rather than the displayed rounded rate. Among eligible rows only, choose smallest variance. With binary cell calculations a value extremely close to a threshold requires a documented exact or tolerance policy; do not automatically round candidate return up. Recompute rows with correlation +.75 without changing their means. Python independently enumerates the declared set and compares a second formula for the sample variance; inspect the rejection reasons as well as the chosen row.

## 5. Statement bridge

Put starting receivables, inventory, and payables in B2:B4 (40,70,35) and ending values in C2:C4 (52,66,35). In B5 use `=B2+B3-B4`, filled right into C5. Put sales, operating expenses, cash-tax rate, depreciation and investment in E2:E6 (300,215,.25,20,38). Before distributions output `=(E2-E3)*(1-E4)+E5-E6-(C5-B5)`. Independently reconstruct the change in cash, net assets and owner equity using Chapter 12's opening positions and stipulated distribution. Do not use cash as a plug. In Python use the actual dated working-capital change and reconcile assets to liabilities and equity in a separate path. Test a late collection: increasing ending receivables by 10 should reduce cash-flow value and ending cash by their specified effects without changing sales.

## 6. Capstone: legal counts, budget, and terminal state floor

In a clean sheet place bond price, equity price, bond terminal payment, equity high payment, equity low payment, budget and terminal floor in B2:B8, in that order (100,100,105,130,85,1000,980). B2 must be traced to the dated model, not accepted just because it is given here to make the recipe reproducible. Put A and B names in A11:A12, bond counts 6 and 8 in B11:B12, and equity counts 4 and 2 in C11:C12. In row 11 use:

| Column | Formula or requirement |
| --- | --- |
| D | `=B11*$B$2+C11*$B$3` initial dollars paid |
| E | `=B11*$B$4+C11*$B$5` high state |
| F | `=B11*$B$4+C11*$B$6` low state |
| G | `=AVERAGE(E11:F11)` mean of exactly the two equal-weight states |
| H | `=AND(COUNT(B11:G11)=6,B11>=0,C11>=0,INT(B11)=B11,INT(C11)=C11,D11=$B$7,MIN(E11:F11)>=$B$8)` feasibility |

Validate B2:B8 as explicit numeric inputs before filling down. This deliberately strict arithmetic budget equality is exact for the stated cases, whose baseline unit prices are 100; if you import real-valued floating formulas, document currency rounding and tolerances rather than pretending displayed cent equality is exact. Copy the row formulas down to the other candidate. Starting from permitted states, change only equity's low payment to 70, then 69. Candidate B should pass exactly at 980 in the first perturbation and fail at 978 in the second. Confirm that higher expected value did not create a passing result. A change in the modeled unit price needs a new budget check without changing what the claim pays. An equivalent exact Python evaluation is included in `check_models.py`. Enter a noninteger count or a missing input as an additional falsification test before trusting a polished output.

[Contents](../README.md)

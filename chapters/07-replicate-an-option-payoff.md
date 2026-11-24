# Replicate an Option Before Pricing Its Story

Two analysts agree a claim pays 20 in one state and zero in the other. They disagree about the probability of the first state. For this one-step model, start by asking whether another package of claims can reproduce both payoffs. That question can determine a price under assumptions that a prediction about the market cannot replace.

## Build the two-state tree

A fictional non-dividend underlying is 100 today, and at the single terminal date it will be either 120 or 80. A European call in this model pays `max(terminal value − 100, 0)`, giving 20 or zero. The risk-free accumulation factor for this one period is 1.05. Assume the two states exhaust the model, borrowing and lending are possible at that rate, fractional holdings permitted, and no trading, financing or settlement friction. These are modeling premises, not available trading terms.

A replicate holds a fraction `d` of the underlying and a risk-free position `B` measured as dollars invested today; negative B denotes borrowing in the model. Solve:

- `120d + 1.05B = 20` in the up state.
- `80d + 1.05B = 0` in the down state.

Subtract the second line from the first to get `40d = 20`, so `d = 0.5`. The down state then requires `1.05B = −40`, and `B = −40/1.05`. Initial cost is about 11.90. Check payoffs by substituting the exact values into **both** rows. If either fails, a plausible initial price doesn't fix the hedge.

## Use a second representation, not a second opinion

A pricing weight chosen so expected underlying terminal value equals 105 is `(105−80)/(120−80) = 0.625`. Applying that weight to the 20 payoff then discounting gives the same 11.90. This is a **risk-neutral pricing weight**, not the asserted chance that the market rises. If the risk-free accumulation were incompatible with the up and down prices, the weighted shortcut would produce an out-of-range probability and the stated no-arbitrage setup needs revisiting. Our model checks that 105 lies strictly between 80 and 120.

Under the stated no-dividend frictionless assumptions the call price lies between `max(100−100/1.05,0)` and 100. A proposed result outside the bounds is a useful warning, but passing the bounds alone does not prove the replicate. No live trading or real option pricing recommendation is made.

**Teardown.** A report multiplies both terminal payoffs by past frequency estimates and calls the result the replication price. Ask where term-by-term equality is shown and whether the averages price the same claim.

**Transfer.** Change the strike to 110, all else unchanged. Compute the two payoffs, the new fraction and financing position, and the price independently from each representation. Show one assumption that must hold for both representations to be equivalent.

[Contents](../README.md)

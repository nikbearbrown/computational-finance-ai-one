# Assessment: An Analyst Model Packet That Can Be Challenged

Use only the fictional inputs below. Record a first calculation by hand or calculator before consulting an assistant. Then implement the same contract in Excel or Python and submit enough detail for someone else to reproduce it. You may use AI to draft, question or critique one part of the implementation after your attempt; a supplied simulated answer or peer critique is equivalent. No account, trade or hosted model is required.

## Model specification

- Valuation date time zero, one terminal date exactly a year later, dollar units, integer units of each claim, no later periods.
- Initial modeled budget $1,000, all used by either candidate, no interim flows or withdrawals, no modeled fees, taxes or transaction frictions.
- A claims-model discount rate of 5% effective annual applies to a zero-coupon claim paying 105 once at the terminal date. The exercise assumes this bond payment in both states.
- A synthetic equity unit costs 100 and pays 130 or 85 at the terminal date. Use weights 0.5 and 0.5 for these two illustrative states. These are model inputs, not inferred odds or promised losses.
- Candidate A holds six bond units and four equity units. Candidate B holds eight bond units and two equity units. A modeled decision must use exactly the budget and receive at least 980 in **each** listed terminal state. Among feasible listed choices prefer the larger modeled expected terminal value. You may decline both if neither is feasible. Do not infer permission to choose an unlisted candidate.

## Tasks

1. Write the model contract and provenance: this case is synthetic; identify the claim each rate or price applies to, unit counts, date, and states. Add a dated hand reconstruction of the zero-coupon price and one state payoff. Explain why an output of 95.24 is suspicious at the base inputs.
2. Implement in Excel or Python using the same dated inputs. Produce a table with initial cost, state payoffs, expected terminal value, feasibility and reason for each candidate. Submit the formulas or code and a record of which input assumptions you changed, if any. A report without its calculation is not the submission.
3. Test the modeling software independently. Multiply the baseline zero price by the gross rate and recover 105, check monotonicity for a higher discount rate, compare one state to a manual total, and explicitly test the lower payoff boundary. A raised bond discount rate changes valuation today; it does not change contractual cash. If price changes the initial cost, flag budget inconsistency instead of silently changing the counts or treating the base allocation as still feasible.
4. Stress the lower equity outcome from 85 to 70; then stress it to 69. Keep counts, initial price and other assumptions unchanged. Describe the case just meeting the floor and the case failing by a small amount. A long sequence of successes does not excuse an error at the boundary.
5. Compare with this supplied simulated output: “A's expected terminal value is larger, so its risk constraint passes. The bond is worth 95.24 because it pays at the end of the first year.” Identify both faults, keep any correctly computed fact, and justify your decision without repeating the model's recommendation as evidence. Name one omitted risk a real analyst would need to check.

## Rubric (25 points)

| Dimension | Evidence for full credit (5 points) |
| --- | --- |
| Assumptions and provenance | Explicit date, units, stated payment, sample/state limits and synthetic evidence |
| Reproducible model | Visible formulas or code for both candidates, exact budget, state values and ranking |
| Independent validation | Hand benchmark and state total, higher-rate check and correct behavior at equality and just below |
| Interpretation | Distinguishes modeled mean from minimum; rejects uncovered risk claims and identifies a meaningful missing input |
| Unaided defense and revision | Preserves first attempt; explains one changed assumption with only the affected outputs recomputed |

Four points: small correctable error that does not affect the decision. Three: meaningful setup with an important gap. Two: partial work with a wrong or unverified decision. One: a claim without recoverable reasoning. Zero: no attempt. Explain one result to another person without access to the model transcript. These are suggested learning criteria, not a deployed course policy.

[Back to contents](../README.md)

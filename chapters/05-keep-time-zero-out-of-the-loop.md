# Keep Time Zero Out of the Future-Value Loop

A cash-flow model includes the right four entries and produces the wrong NPV. The error is not that an amount went missing. One routine treated the outlay today as a payment at the first period end. The other did what the ledger said.

## Make the dates visible

A fictional operation costs 90 at time zero and returns 30, 35 and 45 at the next three annual ends, with the last amount inclusive of every cash flow at closure. There is no cash stream or sale after year three. All figures use the same currency and scale; cash flow must not be switched between dollars and thousands in the middle. Under the exercise's risk and rate assumptions, use 8% effective annually. Doing nothing is the modeled zero alternative.

The single-date comparison is `−90 + 30/1.08 + 35/1.08² + 45/1.08³ ≈ 3.51`. The return of all 110 undiscounted receipts is not the answer. In Excel a periodic NPV formula discounts its first range argument as a period-end cash flow, so add the time-zero amount separately. The explicit dated Python sum can include the order-date flow at exponent 0. Both should agree with a calculator applied to the written schedule. See the [same model in two representations](../labs/two-implementations.md).

At zero discount rate the result is 20. Moving the time-zero expense to year one by mistake still gives 20 at zero. That metamorphic check is useful but insufficient. An exact dated check, plus an example that otherwise has an ambiguous interpretation, is part of the specification. If introducing irregular actual dates, choose a date/basis convention transparently rather than treating one calendar year and one row as always equivalent.

## Refuse free terminal money

A simulated analyst adds 45 as a post-closure continuation value because the latest modeled cash was 45. The dataset says that result is the last period including closure cash. A model of a going concern needs explicit future cash assumptions and a coherent risk and rate basis. Ending a forecasting spreadsheet at year three does not by itself justify either a separate perpetuity or an assumed zero residual. It is the business assumptions that decide which interpretation is valid.

**Teardown.** Frame one correct benchmark and one intentionally wrong date model for this case. Check whether the incorrect model has a higher or lower number when the entire four-row ledger is shifted one period later. A small error in a model total can conceal a complete misunderstanding of the dates.

**Transfer.** Keep the ultimate 45 receipt but defer it to year four. Show exactly which discounted term changes and calculate the new NPV. Explain how a different time-zero cost would interact with this decision without changing the last receipt.

[Contents](../README.md)

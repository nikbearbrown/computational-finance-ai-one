# Reconstruct the Return Before Scaling the Risk

A price series starts at 100 and ends at 95. A fund description says the total loss was about 3.16%. The price change is −5%. Inspect what happened between the dates before deciding the second number must be false.

## Returns with dates and income

This synthetic instrument starts at 100, closes month one at 103 after paying 2 in cash at that month's end, and closes month two at 95 with no further distribution. Prices are assumed measured after distributions and on comparable units. For a period with a distribution at its end, return here is `(end price + cash paid) / start price − 1`.

The month-one return is (103+2)/100−1 = 5%. Month two is 95/103−1 ≈ −7.77%. If distributions are reinvested in fractional units at each period end, multiply the two gross returns. The factor is `1.05 × 95/103 ≈ 0.968447`, a cumulative loss of about 3.16%. If one piece were held throughout and the cash distribution were kept idle, the endpoint would instead be 95+2 = 97. These are different total-return conventions, not rounding disagreements.

The equivalent annual rate from this two-month path is the sixth power of its gross return, minus one, about −17.50%. That is the rate scale that would correspond to repeating the observed two-month pattern six times, not a forecast. A monthly volatility estimate is not an annual series either. Multiplying a monthly standard deviation by the square root of 12 relies on an appropriate return aggregation approximation and uncorrelated increments with matching variance assumptions. A short example does not establish those properties.

A missing price or distribution is not zero. Require a period-matched price and a declared distribution for each row. If the price on a month end is unknown, obtain a trustworthy comparable observation or exclude/relabel affected returns with an explicit date note. Dropping a row without changing the horizon can silently create an annualization error.

## A risk statistic and a path statistic

The next data are a separate fictional wealth path: 100, 110, 99, 121, 96.80, 101.64. At each step, take the maximum value observed up to that step and divide current wealth by it; subtract one. The 99 observation is 10% below its prior high of 110. The 96.80 observation is 20% below 121, the worst drawdown in this path. The last value is about 16% below that same peak. Dividing the minimum value by the final value does not measure maximum drawdown.

Sampling variability is different again. Imagine a toy resampling experiment in which each of two draws independently selects −10% or +10% with replacement and equal probability. The four equally weighted ordered pairs give arithmetic sample means −10%, zero, zero, +10%. Their standard deviation across this toy distribution is about 7.07 percentage points, not 10. Such a resampling exercise models how a statistic varies under a rule; historical financial returns are not shown to be independent or stable merely by computing it.

**Teardown.** A script prints a zero return for an empty distribution cell and compares the reported max drawdown to the worst single-period return. Identify the first data-quality problem and produce a hand ledger showing why the statistics need not agree. An independently checked case can reject a flattering plot.

**Transfer.** Change the wealth sequence's final 101.64 to 91.96. Compute the new current drawdown and maximum drawdown. State whether the same result would tell you how long the portfolio stayed below its previous peak.

[Contents](../README.md)

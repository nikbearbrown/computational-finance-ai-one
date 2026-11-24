# Separate Portfolio Value From the Fund's Trading Price

A fund's underlying assets increased in value. A person who bought and sold its shares over the same interval lost money. Before calling one result false, reconcile which market price and which accounting value each measured.

## State which series your return uses

In a fictional exchange-traded fund the first net asset value (NAV) per share is 50.00 and the quoted trade price is 50.30. At a second matched observation the NAV is 50.10 and the observed trade price is 49.80. We treat the two price observations as actual executable trade prices solely in this exercise, no spreads, distributions or buyer costs. NAV reflects modeled portfolio assets less liabilities divided by shares. The price is the value assigned to the share in the exchange transaction.

| Measure | First date | Second date |
| --- | ---: | ---: |
| NAV per share | 50.00 | 50.10 |
| Market price per share | 50.30 | 49.80 |
| Premium to NAV (`price/NAV − 1`) | +0.60% | about −0.60% |

The return measured from NAV is +0.20%. The trade-price return is 49.80/50.30−1, about −0.99%. The spread between them here comes from the change in the price-to-NAV relationship. One illustration is not an estimate of tracking error or of likely trading results. Price observations at different times from NAV cannot be treated as matched without further evidence.

## Track what the fund's label describes

A collective holding can give an investor access to multiple instruments through one share. Compare what the underlying assets are, how the benchmark is defined, and how fund fees or trading costs are accounted for. In a separate synthetic one-period portfolio with 75% opening allocation earning 1.60% and 25% earning 0.20%, the gross modeled return is 1.25%. If a fee equal to 0.10% of opening portfolio value is charged at period end, the net modeled return is 1.15%. Do not apply this toy expense treatment to a real fund without checking the terms and basis.

A fund holding many names may still concentrate in the same factor, industry or risk. A phrase such as “tracks an index” doesn't say which return series is being tracked or what rebalancing the comparison assumes. Document price, total return and fee conventions separately before attributing a difference.

**Teardown.** A report subtracts a period-end NAV from the prior day's market price, divides by the current price, and calls it outstanding fee drag. Identify the inconsistent series, date, and denominator, and state what would actually be required to estimate a fee effect.

**Transfer.** Keep second NAV at 50.10 but set second price equal to it. Compute the trade-price return and final premium. Is a zero premium on the last date sufficient for the two return series to agree?

[Contents](../README.md)

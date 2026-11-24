# Price Exposure, Not Certainty

An analyst reports an asset beta from four observations. A neat model gives an expected return. The same analyst calls this expected return “the minimum the asset will earn.” The first error is about what the input measures. The second is about what the model promises.

## Estimate one slope and name its sample

Take four invented matched return periods, measured in percentage points:

| Row | Benchmark | Asset |
| --- | ---: | ---: |
| T1 | −4 | −4 |
| T2 | −2 | −3 |
| T3 | 2 | 3 |
| T4 | 4 | 4 |

Means are zero. The centered cross products sum to 44 and squared benchmark returns sum to 40. The ordinary least-squares slope with a free intercept is 1.1 for this sample; the intercept is zero. A check recomputes observed minus fitted return for each row rather than assuming the asset predictably earns 1.1 times any benchmark return. The estimate depends on benchmark choice, sample, units and horizon. It does not establish a mechanism or a permanent exposure. A flat benchmark yields no estimable slope in this specification.

## Use an expected-return model with separate inputs

On a different, explicitly stipulated **annual** valuation basis, take risk-free rate 3%, expected broad-market return 8% and a defensible modeled beta of 1.2. That beta is a scenario input, not the slope just estimated above. The one-factor capital asset pricing model gives:

`3% + 1.2 × (8%−3%) = 9%`.

It is an expected or required-return input under the model, not a guarantee. Notice that the premium is 5%, not the full 8% market return. Putting the full market return in the premium term would add an extra beta-weighted risk-free component. For context see [William Sharpe's original paper](https://doi.org/10.1111/j.1540-6261.1964.tb02865.x). The values here are not derived from the paper or live markets.

A separately specified two-factor illustration might add a second factor exposure of 0.5 times a premium of 2%, yielding 10%, if the factor definitions and estimation basis justify the comparison. Adding another historical correlation is not the same as identifying a priced risk. Document whether the premiums are modeled forecasts or backward-looking sample means and whether the exposures are compatible with them.

**Teardown.** A workbook says “alpha equals the actual return that beat the market in one month” and labels the fitted same-sample intercept as a prediction of guaranteed performance. Ask it to identify excess-return versus total-return conventions, the factor setup, and a test on unseen observations.

**Transfer.** Keep the annual risk-free and market inputs, but use a weakly supported beta range of 0.8 to 1.4. Report the implied one-factor return range. Name one independent observation that would reduce the soundness problem rather than merely increase the number of decimal places.

[Contents](../README.md)

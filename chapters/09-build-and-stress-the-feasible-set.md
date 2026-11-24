# Build and Stress the Feasible Set

An optimization tool presents a low-variance portfolio. It violates the investment committee's minimum modeled return. A second report accepts a higher expected return but exceeds the concentration limit. There is no winner until you state which alternatives are eligible and under what assumptions.

## Define the model rather than trusting the optimizer

This is an invented one-period planning model, not an investment recommendation. Assets A and B have modeled expected returns of 5% and 10%, and standard deviations of 12% and 20%. Base correlation is −0.25. The committee accepts nonnegative weights adding to one, requires B's weight to be between 20% and 50% inclusive, and requires expected return at least 7%. It considers only B weights of 20%, 40%, 50%, or 60%. Choose the *minimum modeled variance* among feasible candidates, not the global minimum over all possible weights.

| Weight in B | Weight in A | Expected return | Reason if excluded |
| ---: | ---: | ---: | --- |
| 20% | 80% | 6.0% | Below return floor |
| 40% | 60% | 7.0% | Feasible |
| 50% | 50% | 7.5% | Feasible |
| 60% | 40% | 8.0% | Above concentration cap |

Use covariance (0.12×0.20×(-0.25)=-0.006) measured in squared decimal returns. At 40% in B, variance is `.60² × .12² + .40² × .20² + 2 × .60 × .40 × (−.006) = .008704`. Expressing the square root in percent gives about 9.33%. At 50% in B it is about 10.30%. In the declared candidate set the 40% portfolio meets the return limit at equality and has lower modeled variance. Rounding a 6.99% expected return up to an displayed 7.0% would not meet an exact requirement; test before rounding.

## Stress a dependence assumption, then a scenario

Set correlation to +0.75 without changing the inputs for the individual assets. The candidate with 40% in B now has variance .020224 and standard deviation about 14.22%. It has the same expected return in this sensitivity because the assumed means were fixed. That is not a prediction that the covariance will change or that means never move when correlations do.

Separately model a period with A at −14% and B at −20%. At the previously selected weights the portfolio loses 16.4% for that period. A variance is not a loss bound; the scenario does not need to be interpreted as one standard deviation. A decision memo may accept lower modeled variance only if additional policy stress tests pass. Both the model's purpose and its missing inputs belong in the record.

**Teardown.** “The output with 60% in B is safest because the return column is highest.” Explain which constraint it violates, and why the optimization target was not mean return. Recompute the eligible rows rather than selecting the highest among them.

**Transfer.** If the required return increases from 7% to 7.5% with everything else fixed, which original candidates remain feasible? Compare the new choice's variance under both correlation assumptions without extrapolating a continuous minimum.

[Contents](../README.md)

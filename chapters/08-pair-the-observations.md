# Pair the Observations Before Measuring Diversification

Two files contain the same four returns for each asset. A spreadsheet sorts one column independently. The means and standard deviations do not change, but the reported way the pair moves together does. A covariance model has a join condition, even when that condition looks like four rows on a sheet.

## Create a paired test small enough to redo

These are four synthetic same-period observations, recorded in percentage points. The row identifiers refer to dates shared by both assets. Use a sample covariance and sample variances, dividing centered sums by (n-1 = 3). Do not claim a four-observation sample is a reliable estimate of a future relationship.

| Matched row | Asset A return | Asset B return | 50/50 portfolio |
| --- | ---: | ---: | ---: |
| P1 | −8 | 6 | −1 |
| P2 | −2 | −6 | −4 |
| P3 | 6 | 10 | 8 |
| P4 | 12 | −2 | 5 |

Means of A and B are both 2. A's centered values are −10, −4, 4, 10; B's are 4, −8, 8, −4. Their products sum to −16, so sample covariance is −16/3 squared percentage points. Their squared deviations sum to 232 and 160, so sample variances are 232/3 and 160/3. Weights (w_A, w_B) enter portfolio variance as:

`w_A² var(A) + w_B² var(B) + 2 w_A w_B cov(A,B)`.

For the 50/50 portfolio this gives 30 squared percentage points. A genuinely different check computes the portfolio return row by row and takes the sample variance of that four-row series. Its mean is 2, centered returns are −3, −6, 6, 3, and their squared sum is 90. The same 30 results. The standard deviation is about 5.48 percentage points, below either asset's sample standard deviation in this illustration.

## Test what is not conserved by a row error

Reverse the order of B's four values but leave A unchanged. Both single-asset columns still have the same mean and dispersion as before. Now the centered cross products sum to +16, not −16, and the computed portfolio sample variance changes. That rearrangement is an intentionally invalid pairing, not a legitimate way to improve or stress the fund. A valid stress scenario explicitly changes a dependence assumption. It does not silently drop the evidence of dates.

A useful verification record specifies observation time, return basis, paired rows retained, and treatment of missing data. If a date is missing in one column, a complete-pair estimator can drop the corresponding whole observation with the reason logged. Silently filling a blank with zero creates a new synthetic outcome. Matching a month-end return with a year-end outcome without checking horizons creates a different problem.

**Teardown.** A report says both asset histograms are unchanged and uses that as proof tomorrow's risk panel is right. Ask for a pair-by-pair reconstruction and an independently computed weighted series. Explain which statistics the y-axis units represent.

**Transfer.** Compute sample portfolio variance after reversing B in the intentionally incorrect pairing. Then identify a data-handling rule that would prevent the error in the first place.

[Contents](../README.md)

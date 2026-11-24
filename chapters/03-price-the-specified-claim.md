# Price the Claim, Not the Label

At the same date a debt claim and an equity claim both have modeled prices. Running one discount routine on both does not make the cash flows or the rates equivalent. Start by naming which holder receives which dollars.

## A coupon bond and its rate sensitivity

A fictional two-year bond, valued just after a coupon date, has face 100 and pays 6 at the end of each year. The last payment also includes principal. Assume the payments are made as promised, no fee, accrued interest, early redemption, or alternative payment schedule. Use an effective annual yield of 5%.

`P = 6/1.05 + 106/1.05² ≈ 101.86`.

The coupon rate is 6% of face; the yield is the rate that prices the promised stream, not a second coupon. Set the yield to 6% and the price is 100 in the assumed timing convention. Rate sensitivity can be summarized locally by weighting the two dates by their discounted cash contributions. This **Macaulay duration** is `(1×PV(6) + 2×PV(106)) / P ≈ 1.9439 years`. It lies between the two payment dates and is pulled toward the larger final payment.

With annual compounding, modified duration here is Macaulay duration divided by 1.05, about 1.8513. For a yield change of +0.01, the first-order relative price change is about −1.85%. Exact repricing at 6% gives a decline of about 1.83% from the 5% valuation. The approximation is not exact because the price curve bends. A cash flow's size and date are both relevant.

## A share needs a different story

A bond has a prescribed payment schedule under the model. A common share is a residual claim; a dividend forecast is not the same obligation. For a separate fictional share, assume expected dividend next year of 2.80, growth 3.5% in perpetuity consistent with the distribution path, and a 9% required return on the modeled equity. The constant-growth value is `2.80/(0.09−0.035) ≈ 50.91`. If growth equals or exceeds the discount rate, that infinite-series shortcut is invalid. Do not choose inputs simply to produce a high price.

This is a comparison of modeling mechanics, not how to select an actual security. Duration measures sensitivity to a particular yield change under the stated bond model. It does not capture every credit, liquidity or cash-flow change.

**Teardown.** A workbook labels the bond rate “coupon yield,” puts 6 in the final payment row, and omits the 100 principal. Find the two financial assumptions obscured by that label and design a par-price check that exposes the omission.

**Transfer.** Replace the bond with a two-year zero paying 100 at maturity, leaving all conventions unchanged. What is its Macaulay duration? Why does the cash-date check work without knowing the price to the cent?

[Contents](../README.md)

# Computational Finance (AI Plus One)

**Original compact course rough 0.1.** Thirteen chapters, shared synthetic cases and a reproducible capstone. Not an expert-edited replacement for an existing book or an adopted course.

For MBA or advanced undergraduate learners comfortable with present value, returns and either Excel or introductory Python. This is one book about building a defensible instrument, risk or portfolio model. It is not an introduction to personal finance, an inside-the-firm corporate capital-allocation book, a programming manual or a trading guide. No live trading, hosted AI, account connection, real financial data or personalized advice is part of the exercises.

Start with a financial question and a dated hand check. Implement the same contract in Excel or Python. Use the other representation or a genuinely independent simple calculation to find what the first one missed. Discuss exactly which result would change the decision, and which facts the setup doesn't know. The flawed answers labeled in the chapters are fabricated for practice.

## Build and inspect the instrument model

- 01. [Specify the Financial Question Before Building the Model](chapters/01-specify-the-financial-question.md)
- 02. [Reconstruct the Return Before Scaling the Risk](chapters/02-reconstruct-returns-and-risk.md)
- 03. [Price the Claim, Not the Label](chapters/03-price-the-specified-claim.md)
- 04. [Separate Portfolio Value From the Fund's Trading Price](chapters/04-separate-fund-nav-from-price.md)
- 05. [Keep Time Zero Out of the Future-Value Loop](chapters/05-keep-time-zero-out-of-the-loop.md)
- 06. [Separate Asset Risk From Account Risk](chapters/06-separate-asset-and-account-risk.md)
- 07. [Replicate an Option Before Pricing Its Story](chapters/07-replicate-an-option-payoff.md)

## Measure risk in portfolios

- 08. [Pair the Observations Before Measuring Diversification](chapters/08-pair-the-observations.md)
- 09. [Build and Stress the Feasible Set](chapters/09-build-and-stress-the-feasible-set.md)
- 10. [Allocate the Risky Budget, Then Rebalance the Holdings](chapters/10-allocate-and-rebalance.md)
- 11. [Price Exposure, Not Certainty](chapters/11-price-exposure-not-certainty.md)

## Reconcile and defend the decision

- 12. [Connect Statements to the Forecast, Not to a Headline](chapters/12-connect-statements-to-the-forecast.md)
- 13. [Defend the Model When the Attractive Answer Fails](chapters/13-defend-the-model-when-it-fails.md)

## Lab tools and assessment

- [Excel and Python recipes](labs/two-implementations.md): same inputs, same outcomes, practical checks. Spreadsheet steps are recipes, not a bundled or runtime-tested workbook.
- [Synthetic inputs](data/synthetic-labs.json) and [the offline Python check](scripts/check_models.py). Standard library only: `python3 -I -B scripts/check_models.py`. It validates the case computations, not the appropriateness of their assumptions or another tool's results.
- [Analyst model packet and scoring rubric](assessment/analyst-model-packet.md): dated valuation, budget, two modeled states, exact boundaries, independent verification and an unaided decision defense.

The course rough remains subject to deeper examples, expert editing, format and accessibility testing, and any separate adoption decision.

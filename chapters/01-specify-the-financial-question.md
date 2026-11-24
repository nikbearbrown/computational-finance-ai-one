# Specify the Financial Question Before Building the Model

A model values an instrument at 95.24. Its chart is smooth, its rate input is labeled 5%, and a second tool gives the same answer. The instrument pays 105 one year from today. Before congratulating the tools for agreeing, see what date produces 95.24.

This course is for learners who already know basic present value and return, and are comfortable with one of Excel or introductory Python. It teaches you to build and challenge the same financial model in either representation. No live data, investment account, trade execution, or AI subscription is needed.

## Make a model contract

Write the question as a claim, comparison, and decision: “What should the modeled price be today for one cash flow of 105 at the end of year one using a 5% effective annual discount rate?” Then state the financial assumptions: one unit of the claim; no intermediate payment; no settlement offset, taxes, fees or default in this example; currency stays the same. The model cannot decide what you meant by “one year.”

| Model item | Declared value | How to check it |
| --- | --- | --- |
| Price date | Time 0 | First date in the ledger |
| Cash flow | 105 at time 1 | No cash flow at time 0 or time 2 |
| Effective annual rate | 0.05 | Not the number 5 |
| Benchmark price | 100 | Multiply by 1.05 and recover 105 |

Divide once: 105/1.05 = 100. The erroneous price 95.24 is close to 105/1.05². That is evidence of a timing hypothesis, not a conclusion about which line caused the error. The equivalent spreadsheet and Python expressions are given in the [lab recipes](../labs/two-implementations.md). Build one. A second implementation may be useful if its method and setup are independently checked, not copied from the same report.

## Turn assumptions into tests

At 0% this instrument is worth 105. At 10% it is worth about 95.45. For positive future receipts at fixed dates, price should fall when the discount rate rises. That direction test cannot detect every wrong exponent: discounting twice gives the same direction. Pair invariants with a priced benchmark and also test a deliberately wrong input.

When an agent helps write a formula, give it a schema and tests rather than a request for “the answer.” Ask for one implementation and explicit handling of input failures. Keep the original data, a copy of each changed assumption, and one independent calculation you could defend without reading a transcript. Do not feed in accounts, positions, customer records or current confidential data. You can do all steps with a calculator and the provided fictional material.

**Teardown.** Find why equal outputs did not verify the model. Rebuild the one-period price on paper and then show one invalid entry that either implementation should reject or visibly flag.

**Transfer.** Make the payment genuinely due in two years at the same annual rate. The old “wrong” answer may now be correct. Explain how a change to the model contract differs from fixing a calculation.

[Contents](../README.md)

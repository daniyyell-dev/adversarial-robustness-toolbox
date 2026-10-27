I have prepared an implementation in **REPLACE_WITH_PR_LINK_AFTER_CREATING_THE_PR**, covering L2/Linf, targeted and untargeted FMN, ART integration, tests and a real-digits CPU example.

A real digit originally predicted as 0 is predicted as 6 after the L2 attack. The first four selected held-out samples are shown below, with the actual pixel changes. The full 100-sample evaluation includes both successful and unsuccessful searches; results and limitations are in the [review evidence](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/review/fmn-contribution/contrib/fmn-review).

![Real FMN samples and pixel changes](https://raw.githubusercontent.com/daniyyell-dev/adversarial-robustness-toolbox/refs/heads/review/fmn-contribution/contrib/fmn-review/digits-mlp/samples-l2.png)

The new attack tests pass with full statement/branch coverage. Feedback on the initial scope and estimator integration would be welcome.

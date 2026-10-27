I have prepared an implementation in https://github.com/Trusted-AI/adversarial-robustness-toolbox/pull/2856, covering L2/Linf, targeted and untargeted FMN, ART integration, tests and a real-digits CPU example.

A real digit originally predicted as 0 is predicted as 6 after the L2 attack. The first four selected held-out samples are shown below, with the actual pixel changes. The full 100-sample evaluation includes both successful and unsuccessful searches; results and limitations are in the [review evidence](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/5357e2683eef6d09355058dafb78621a92f05bda/contrib/fmn-review).

![Real FMN samples and pixel changes](https://raw.githubusercontent.com/daniyyell-dev/adversarial-robustness-toolbox/5357e2683eef6d09355058dafb78621a92f05bda/contrib/fmn-review/digits-mlp/samples-l2.png)

The new attack tests pass with full statement/branch coverage. Feedback on the initial scope and estimator integration would be welcome.

The attack is from Pintor, Roli, Brendel and Biggio, [Fast Minimum-norm Adversarial Attacks through Adaptive Norm Constraints (NeurIPS 2021)](https://proceedings.neurips.cc/paper_files/paper/2021/hash/a709909b1ea5c2bee24248203b1728a5-Abstract.html), with the authors’ MIT-licensed source credited in the implementation.

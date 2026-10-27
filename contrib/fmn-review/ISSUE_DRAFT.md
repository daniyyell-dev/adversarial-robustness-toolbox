# Title: Add Fast Minimum-Norm (FMN) attack with L2 and Linf support

I would like to contribute an ART implementation of Fast Minimum-Norm (FMN), from [Pintor et al., NeurIPS 2021](https://arxiv.org/abs/2102.12827). I could not find an existing FMN implementation or matching proposal when checking the current main branch and issues/PRs.

The proposed initial scope is L2 and Linf, with targeted/untargeted attacks, ART class-logit gradients, batching, bounded inputs, tests and a small real-data example. L0/L1, restarts and adversarial initialisation would remain outside this first implementation. The authors' [MIT-licensed implementation](https://github.com/pralab/Fast-Minimum-Norm-FMN-Attack) is credited, with copyright/licence notices preserved.

A working implementation is available in [my fork](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/feature/fast-minimum-norm), with [test results and reproducible samples](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/review/fmn-contribution/contrib/fmn-review). On 100 correctly classified held-out handwritten digits using a trained small MLP, the ART implementation and original author source both achieved:

- L2: 82/100 untargeted and 97/100 targeted successes.
- Linf: 100/100 untargeted and targeted successes.

These are CPU smoke evaluations at 100 iterations, not paper-scale benchmarks. The review also records unsuccessful cases and a linear-model convergence limitation.

For example, the first real digit below is predicted as 0 before perturbation and 6 afterwards:

![L2 sample inputs, outputs and pixel changes](https://raw.githubusercontent.com/daniyyell-dev/adversarial-robustness-toolbox/refs/heads/review/fmn-contribution/contrib/fmn-review/digits-mlp/samples-l2.png)

Would this L2/Linf scope be useful as an initial FMN contribution to ART?

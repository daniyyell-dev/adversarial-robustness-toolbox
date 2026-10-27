I would like to contribute an ART implementation of Fast Minimum-Norm (FMN), from [Pintor et al., NeurIPS 2021](https://arxiv.org/abs/2102.12827). I could not find an existing FMN implementation or matching proposal when checking the current main branch and issues/PRs.

The proposed initial scope is L2 and Linf, with targeted/untargeted attacks, ART class-logit gradients, batching, bounded inputs, tests and a small real-data example. L0/L1, restarts and adversarial initialisation would remain outside this first implementation. The authors' [MIT-licensed implementation](https://github.com/pralab/Fast-Minimum-Norm-FMN-Attack) is credited, with copyright/licence notices preserved.

A working implementation is available in [my fork](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/feature/fast-minimum-norm), with [test results and reproducible samples](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/5357e2683eef6d09355058dafb78621a92f05bda/contrib/fmn-review). On 100 correctly classified held-out handwritten digits using a trained small MLP, the ART implementation and original author source both achieved:

- L2: 82/100 untargeted and 97/100 targeted successes.
- Linf: 100/100 untargeted and targeted successes.

These are CPU smoke evaluations at 100 iterations, not paper-scale benchmarks. The review also records unsuccessful cases and a linear-model convergence limitation.

For example, the first real digit below is predicted as 0 before perturbation and 6 afterwards:

![L2 sample inputs, outputs and pixel changes](https://raw.githubusercontent.com/daniyyell-dev/adversarial-robustness-toolbox/5357e2683eef6d09355058dafb78621a92f05bda/contrib/fmn-review/digits-mlp/samples-l2.png)

Would this L2/Linf scope be useful as an initial FMN contribution to ART?

## Reference

Maura Pintor, Fabio Roli, Wieland Brendel, and Battista Biggio. **Fast Minimum-norm Adversarial Attacks through Adaptive Norm Constraints.** Advances in Neural Information Processing Systems 34 (NeurIPS 2021).

- [Published paper](https://proceedings.neurips.cc/paper_files/paper/2021/hash/a709909b1ea5c2bee24248203b1728a5-Abstract.html)
- [arXiv:2102.12827](https://arxiv.org/abs/2102.12827)
- [Authors' MIT-licensed implementation, pinned to the version used for validation](https://github.com/pralab/Fast-Minimum-Norm-FMN-Attack/tree/98c68c26aaa72e4259634b94308b6a2db236a38a)

This contribution implements the published method; credit for the attack belongs to the paper's authors.

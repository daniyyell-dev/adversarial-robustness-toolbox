# Title: Add L2 and Linf Fast Minimum-Norm evasion attack

# Description

Adds `FastMinimumNorm`, an implementation of [Pintor et al.'s FMN attack (NeurIPS 2021)](https://arxiv.org/abs/2102.12827), using ART classifier logits and class gradients. FMN adapts a per-sample norm constraint while searching for small successful perturbations. This initial implementation supports L2/Linf, targeted/untargeted modes, batching, and finite scalar or featurewise bounds. It retains the smallest successful evaluated example and returns the original input on failure.

Related feature issue: **insert the issue link after opening it**.

No new core dependencies. The attack itself uses NumPy and ART's estimator interface. A real-digits CPU example uses existing optional PyTorch/scikit-learn integrations; comparison with the original author source additionally requires Foolbox/EagerPy.

Maura Pintor's original MIT-licensed implementation is credited and its copyright/licence notice is preserved. Numerical safeguards handle zero gradients, finite bounds, float32 boundary rounding and dtype preservation. As in the reference, the final update is not evaluated for inclusion in the returned result. L0/L1, restarts and adversarial starting points are not part of this change.

## Type of change

- [x] New feature (non-breaking)
- [x] This change requires a documentation update

# Testing

- [x] Deterministic analytical distance, targeting, batching, input/output, rounding and failure tests.
- [x] Real ART PyTorch estimator; optional independent Foolbox Linf comparison.
- [x] Real handwritten digits example: 1,347 training / 450 held-out samples; 431/450 clean test accuracy; first 100 correctly classified held-out samples attacked at 100 iterations.

| Mode | ART successes | Median successful norm | Original author source successes | Reference median norm |
|---|---:|---:|---:|---:|
| l2_untargeted | 82/100 | 0.502982 | 82/100 | 0.502980 |
| l2_targeted | 97/100 | 0.819099 | 97/100 | 0.818266 |
| linf_untargeted | 100/100 | 0.096243 | 100/100 | 0.096242 |
| linf_targeted | 100/100 | 0.164773 | 100/100 | 0.164940 |

The author reference and ART agreed on success/failure for every sample in all four modes. Outputs are bounded. Per-sample optimization paths are not bit-identical: median norm differences were approximately 1e-6, with maximum targeted norm differences of 0.108775 (L2) and 0.014553 (Linf). A separate linear-model test found no L2 untargeted successes for either implementation under these settings; that limitation is retained in the [full review evidence](https://github.com/daniyyell-dev/adversarial-robustness-toolbox/tree/review/fmn-contribution/contrib/fmn-review). These results do not claim fixed-epsilon robust accuracy or reproduce the full paper benchmarks.

The first four selected real samples show the original digit, changed prediction and pixel differences:

![FMN L2 examples](https://raw.githubusercontent.com/daniyyell-dev/adversarial-robustness-toolbox/refs/heads/review/fmn-contribution/contrib/fmn-review/digits-mlp/samples-l2.png)

**Test configuration:** macOS ARM64; ART base `19c914495be197a9ab316ac4a36de8080ce339d2`; Python 3.13.13, NumPy 2.5.4, PyTorch 2.13.0; CPU. Nine test methods passed; new attack statement and branch coverage is 100%. NumPy-only tests also passed on Python 3.10.20 / NumPy 1.26.4 (eight passed, optional PyTorch test skipped). Full-tree Ruff and changed-file Black/pycodestyle passed; targeted mypy passed; targeted pylint scored 10/10 with the existing invalid config option disabled. No GPU/full-framework test suite was run; optional Foolbox import emits an existing SciPy deprecation warning.

# Checklist

- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] I have commented my code
- [x] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings (optional reference import has an existing SciPy deprecation warning)
- [x] I have added tests that prove my feature works
- [ ] New and existing unit tests pass locally with my changes (new focused tests pass; full framework suite not run)
- [ ] My changes have been tested using both CPU and GPU devices (CPU only)

"""Render the first four evaluated digits with original, adversarial and difference views."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent / 'digits-mlp'
report = json.loads((root / 'results.json').read_text())
samples = np.load(root / 'samples.npz')
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
for norm in ('l2', 'linf'):
    key = norm + '_untargeted'
    result = next(item for item in report['results'] if item['attack'] == key)
    fig, axes = plt.subplots(4, 3, figsize=(10, 11), constrained_layout=True)
    for row in range(4):
        original = samples['x'][row].reshape(8, 8)
        adversarial = samples[key][row].reshape(8, 8)
        label = int(samples['y'][row])
        prediction = result['sample_predictions'][row]
        axes[row, 0].imshow(original, cmap='gray', vmin=0, vmax=1, interpolation='nearest')
        axes[row, 0].set_title(f'Original digit {label}\nPrediction: {label}', fontsize=11)
        axes[row, 1].imshow(adversarial, cmap='gray', vmin=0, vmax=1, interpolation='nearest')
        axes[row, 1].set_title(f'FMN prediction: {prediction}\n{norm.upper()} distance: {result["sample_norms"][row]:.4f}', fontsize=11)
        image = axes[row, 2].imshow(adversarial-original, cmap='RdBu_r', vmin=-0.25, vmax=0.25, interpolation='nearest')
        axes[row, 2].set_title('Pixel changes\nSeparate colour scale', fontsize=11)
        for axis in axes[row]:
            axis.set_xticks([])
            axis.set_yticks([])
    fig.colorbar(image, ax=axes[:, 2], shrink=0.75, label='Pixel change (input units)')
    fig.suptitle(f'FMN {norm.upper()} on real held-out digits\nFirst four selected samples; 100 iterations on CPU', fontsize=15)
    fig.savefig(root / f'samples-{norm}.png', dpi=140)
    plt.close(fig)
# Keep one unsuccessful case visible: failures return the unchanged original, not an unverified adversarial sample.
failed = np.flatnonzero(np.all(samples['l2_untargeted'] == samples['x'], axis=1))
if len(failed):
    index = int(failed[0])
    fig, axes = plt.subplots(1, 2, figsize=(7, 4), constrained_layout=True)
    label = int(samples['y'][index])
    for axis, key, title in zip(axes, ('x', 'l2_untargeted'), ('Original', 'Returned after failed L2 search')):
        axis.imshow(samples[key][index].reshape(8, 8), cmap='gray', vmin=0, vmax=1, interpolation='nearest')
        axis.set_title(f'{title}\nPrediction: {label}')
        axis.set_xticks([])
        axis.set_yticks([])
    fig.suptitle(f'Unsuccessful example: selected sample {index + 1}, true digit {label}')
    fig.savefig(root / 'failure-l2.png', dpi=140)
    plt.close(fig)

import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

json_file = 'data_for_graphic2.json'

with open(json_file, 'r') as f:
    avg_cnots = np.array(json.load(f))


plt.figure(figsize=(12, 8))

row_indices = np.arange(avg_cnots.shape[0])[:, np.newaxis]

mask_for_special = avg_cnots <= row_indices
mask_for_normal  = avg_cnots > row_indices


sns.heatmap(avg_cnots, mask=mask_for_normal, cmap='viridis', annot=False, cbar=True)
sns.heatmap(avg_cnots, mask=mask_for_special, cmap=ListedColormap(['#A52A2A']), annot=False, cbar=False)

plt.title("AVG_CNOT_COUNT heatmap", fontsize=18)
plt.xlabel("Размер матрицы N", fontsize=14)
plt.ylabel("Количество шагов K", fontsize=14)

sns.despine(left=True, bottom=True)
plt.gca().invert_yaxis()

output_file = "cnot_colored_heatmap.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')

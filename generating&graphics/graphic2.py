import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

json_file = 'data_for_graphic2.json'

with open(json_file, 'r') as f:
    avg_cnots = np.array(json.load(f))


plt.figure(figsize=(12, 8))
sns.heatmap(avg_cnots, annot=False, cmap="viridis")

plt.title("AVG_CNOT_COUNT heatmap", fontsize=18)
plt.xlabel("Размер матрицы N", fontsize=14)
plt.ylabel("Количество шагов K", fontsize=14)

sns.despine(left=True, bottom=True)
plt.gca().invert_yaxis()

output_file = "cnot_heatmap.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import json


json_file = 'data_for_graphic3.json'

with open(json_file, 'r') as f:
    avg_cnots = np.array(json.load(f))

plt.Figure(figsize=(14, 12))

k = np.arange(0, avg_cnots.shape[0])
y = avg_cnots[2:] / k[2:]

sns.set_theme(style="whitegrid", context="paper")
sns.despine(left=True, bottom=True)
sns.lineplot(x=k[2:], y=y, linewidth=2.5, color='blue')

plt.title('Зависимость cnot_count / k от k при n=20', fontsize=15)
plt.xlabel('Количество шагов k', fontsize=14)
plt.ylabel('CNOT_count / k', fontsize=14)

output_file = 'cnot_steps_devided.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()
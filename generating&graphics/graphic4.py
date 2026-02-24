import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import json


json_file1 = 'data_for_graphic1.json'
json_file2 = '../Min_Lin_Com/data_for_graphic4.json'

with open(json_file1, 'r') as f:
    avg_cnots1 = np.array(json.load(f))

with open(json_file2, 'r') as f:
    avg_cnots2 = np.array(json.load(f))


plt.Figure(figsize=(16, 9))

n = np.arange(0, avg_cnots1.shape[0])

sns.set_theme(style="whitegrid", context="talk")
sns.despine(left=True, bottom=True)

sns.lineplot(x=n[2:], y=avg_cnots1[2:], linewidth=2.5, color='blue', label='Квантовый метод')
sns.lineplot(x=n[2:], y=avg_cnots2[2:], linewidth=2.5, color='red', label='Криптографический метод')

plt.title('Сравнение квантового и криптографического метода')
plt.xlabel('n')
plt.ylabel('CNOT_count')

output_file = 'methods_comparing.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()
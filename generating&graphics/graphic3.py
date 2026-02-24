import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import json


json_file = 'data_for_graphic1.json'

with open(json_file, 'r') as f:
    avg_cnots = np.array(json.load(f))

print(avg_cnots.shape)

plt.Figure(figsize=(16, 9))

n = np.arange(0, avg_cnots.shape[0])

y1 = n ** 2 / np.log(n)
c = avg_cnots[2:] / y1[2:]

sns.set_theme(style="whitegrid", context="talk")
sns.despine(left=True, bottom=True)
sns.lineplot(x=n[2:], y=c, linewidth=2.5, color='blue')

plt.title(r'Коэффициент пропорциональности в O($\frac{n^2}{logn}$)')
plt.xlabel('n')
plt.ylabel('c')

output_file = 'cnot_coef.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()
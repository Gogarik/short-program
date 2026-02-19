import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

json_file = 'data_for_graphic1.json'

with open(json_file, 'r') as f:
    avg_cnots = np.array(json.load(f))

n_values = np.arange(len(avg_cnots))
avg_cnots = avg_cnots[2:]
n_values = n_values[2:]

sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(12, 7))
sns.lineplot(x=n_values, y=avg_cnots, 
                linewidth=2.5, color='#2980b9', label='Экспериментальные данные')

theory_y = y=n_values ** 2 / np.log(n_values)
sns.lineplot(x=n_values, y=theory_y, linewidth=2, color='red',
                label=r'Аппроксимирующая кривая y = $\frac{n^2}{logn}$')

plt.title("Зависимость среднего числа CNOT от размера матрицы N", 
            fontsize=18, pad=20, fontweight='bold')
plt.xlabel("Размер матрицы (N)", fontsize=14)
plt.ylabel("Среднее число вентилей CNOT", fontsize=14)

plt.legend(frameon=True, loc='upper left')
sns.despine(left=True, bottom=True)

output_file = "cnot_complexity.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()


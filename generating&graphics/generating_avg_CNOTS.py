import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

import json
import numpy as np
from Decomp import decomposition as dec

def generate_avg_CNOTS(matrix_count, n_max):

    avg_CNOT_counts = np.zeros(n_max, dtype=int)

    for n in range(2, n_max):
        link = f'random_matrices/matrix({n}x{n})_{matrix_count}.json'

        with open(link, 'r') as f:
            all_matrices = np.array(json.load(f))

        CNOTS = np.zeros(matrix_count, dtype=int)

        for i in range(matrix_count):
            output = dec.CNOT_Synth(all_matrices[i])
            CNOTS[i] = len(output[0]) + len(output[1])

        avg_CNOT_counts[n] = np.average(CNOTS)

    with open(f'data_for_graphic1.json', 'w') as f:
        json.dump(avg_CNOT_counts.tolist(), f)
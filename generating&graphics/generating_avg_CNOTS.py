import sys
import os
from tqdm import tqdm

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

import json
import numpy as np
from Decomp import decomposition as dec

def generate_avg_CNOTS(matrix_count, n_max, type='random', **kwargs):


    if type == 'random':
        folder = 'random_matrices'

        avg_CNOT_counts = np.zeros(n_max, dtype=int)

        for n in tqdm(range(2, n_max)):
            link = f'{folder}/matrix({n}x{n})_{matrix_count}.json'

            with open(link, 'r') as f:
                all_matrices = np.array(json.load(f))  # implies all matrices at n by matrix_count

            CNOTS = np.zeros(matrix_count, dtype=int)

            for i in range(matrix_count):
                output = dec.CNOT_Synth(all_matrices[i])
                CNOTS[i] = len(output[0]) + len(output[1])

            avg_CNOT_counts[n] = np.average(CNOTS)

        with open(f'data_for_graphic1.json', 'w') as f:
            json.dump(avg_CNOT_counts.tolist(), f)
        

    elif type == 'by_step':

        folder = 'by_step_matrices'
        k_max = kwargs['k_max']
        single_n = kwargs['single_n']

        if (not single_n):

            avg_CNOT_counts = np.zeros((k_max, n_max), dtype=int)

            for n in tqdm(range(2, n_max)):
                for k in range(1, k_max):
                    link = f'{folder}/matrix({n}x{n})_{matrix_count}_{k}.json'

                    with open(link, 'r') as f:
                        all_matrices = np.array(json.load(f))  # Implies all matrices at (n, k) by matrix_count

                    CNOTS = np.zeros(matrix_count, dtype=int)

                    for i in range(matrix_count):
                        output = dec.CNOT_Synth(all_matrices[i])
                        CNOTS[i] = len(output[0]) + len(output[1])

                    avg_CNOT_counts[k][n] = np.average(CNOTS)
            
            with open(f'data_for_graphic2.json', 'w') as f:
                json.dump(avg_CNOT_counts.tolist(), f)

        else:
            avg_CNOT_counts = np.zeros(k_max, dtype=int)
            n_max -= 1

            for k in tqdm(range(1, k_max)):
                link = f'{folder}/matrix({n_max}x{n_max})_{matrix_count}_{k}.json'

                with open(link, 'r') as f:
                    all_matrices = np.array(json.load(f))

                CNOTS = np.zeros(matrix_count, dtype=int)

                for i in range(matrix_count):
                    output = dec.CNOT_Synth(all_matrices[i])
                    CNOTS[i] = len(output[0]) + len(output[1])

                avg_CNOT_counts[k] = np.average(CNOTS)

                with open(f'data_for_graphic3.json', 'w') as f:
                    json.dump(avg_CNOT_counts.tolist(), f)

if __name__ == '__main__':
    generate_avg_CNOTS(n_max=120, matrix_count=30, type='random')
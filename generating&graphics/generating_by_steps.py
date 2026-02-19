import numpy as np
import json

def generate_data2(k, matrix_count, n):
    first  = np.random.randint(0, n, (k, matrix_count))
    second = (first + np.random.randint(1, n, (k, matrix_count))) % n

    res = np.tile(np.eye(n, dtype=np.uint8), (matrix_count, 1, 1))
    r = np.arange(matrix_count)

    for j in range(k):
        res[r, first[j]] ^= res[r, second[j]]

    with open(f'by_step_matrices/matrix({n}x{n})_{matrix_count}_{k}.json', 'w') as f:
        json.dump(res.tolist(), f)

import numpy as np

def generate_dataset(cnot_count, N, n):
    first  = np.random.randint(0, n, (cnot_count, N))
    second = (first + np.random.randint(1, n, (cnot_count, N))) % n

    res = np.tile(np.eye(n, dtype=np.uint8), (N, 1, 1))
    r = np.arange(N)

    for j in range(cnot_count):
        res[r, first[j]] ^= res[r, second[j]]

    return res
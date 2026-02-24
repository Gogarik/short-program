import numpy as np
import json
import galois
from tqdm import tqdm


GF = galois.GF(2)

def generate_invertible_binary_matrix_gf2(n):
    
    while True:
        matrix = GF.Random((n, n))
        if np.linalg.det(matrix) != 0: 
            return np.array(matrix, dtype=int)
        

def generate_data1(n, matrix_count):

    all_matrix = np.zeros((matrix_count, n, n), dtype=int)
    for i in range(matrix_count):
        all_matrix[i] = generate_invertible_binary_matrix_gf2(n)
    
    with open(f'random_matrices/matrix({n}x{n})_{matrix_count}.json', 'w') as f:
        json.dump(all_matrix.tolist(), f)


    
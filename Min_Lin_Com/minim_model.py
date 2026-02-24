import numpy as np
import json
import math
from itertools import combinations
from tqdm import tqdm


def find_min_CNOT_count(matrix: np.ndarray):

    m, n = matrix.shape
    CNOTS = list()

    S = list(np.eye(n, dtype=int))
    dist = np.sum(matrix, axis=1) - 1

    while (dist.any()):
        max_vec = np.zeros(n)
        final_reduced_indexes = np.full(m, False, dtype=bool)
        CNOT = (0, 0)
        
        # find new base element
        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                new_elem = (S[i] + S[j]) % 2
                reduced_indexes = np.full(m, False, dtype=bool)

                for k in range(m):
                    d = dist[k]
                    
                    if d == 0:
                        continue
                    elif (d == 1):
                        if (np.array_equal(new_elem, matrix[k])):
                            reduced_indexes[k] = True
                            continue
                    else:
                        idx_pairs = np.array(list(combinations(range(len(S)), d - 1)))

                        for l in range(len(idx_pairs)):
                            flag = False
                            vector = new_elem
                            for index in idx_pairs[l]:
                                vector = (vector + S[index]) % 2
                                if (np.array_equal(vector % 2, matrix[k])):
                                    reduced_indexes[k] = True
                                    flag = True
                                    break
                            if flag:
                                break

                
                if (np.count_nonzero(reduced_indexes) > np.count_nonzero(final_reduced_indexes)):
                    max_vec = new_elem
                    final_reduced_indexes = reduced_indexes
                    CNOT = (i, j)

                elif np.count_nonzero(reduced_indexes) == np.count_nonzero(final_reduced_indexes):

                    if (np.linalg.norm(new_elem) > np.linalg.norm(max_vec)):
                        max_vec = new_elem
                        final_reduced_indexes = reduced_indexes
                        CNOT = (i, j)

        S.append(max_vec)
        dist[final_reduced_indexes] -= 1
        CNOTS.append(CNOT)
    
    return CNOTS
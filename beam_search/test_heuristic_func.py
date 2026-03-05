import numpy as np

def test_heuristic(matrix: np.ndarray) -> int:
    sums = matrix.sum(axis=(1, 2))
    traces = np.diagonal(matrix, axis1=1, axis2=2).sum(axis=1)
    n = matrix.shape[1]
    return sums - traces + (n - traces)

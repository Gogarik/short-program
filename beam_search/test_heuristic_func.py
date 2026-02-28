import numpy as np

def test_heuristic(matrix: np.ndarray) -> int:
    return matrix.sum() - matrix.trace() + (matrix.shape[0] - matrix.trace())
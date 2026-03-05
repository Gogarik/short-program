import numpy as np
import test_heuristic_func
import heapq
from typing import Callable
import heapq
from itertools import count
import textwrap

def get_neighbours_vectorized(matrix): # векторизованный вариант получения соседних вершин с данной
    n = matrix.shape[0]
    cnot_from = []

    for j in range(n):
        cnot_from.append(f"{j}")
    all_neighbors = []
    cnots = []

    for i in range(n):
        cnot_to = [f"{i}"] * n # генерируем заранее известную последовательность cnot-ов (по порядку)
        cnots.append(np.delete((np.array(cnot_from) + np.array(cnot_to)), i))

        base = matrix.reshape((1, n, n))
        additional = np.zeros((n, n, n), dtype=np.uint8)
        additional[:, i, :] = matrix.reshape((n, n))
        all_neighbors.append(np.delete(base ^ additional, i, axis=0))

    return np.concatenate(cnots), np.concatenate(all_neighbors, axis=0)


def beam_search(given_matrix: np.ndarray, beam_width: int, heuristic_func: Callable[[np.ndarray], int]) -> np.ndarray:
    n = given_matrix.shape[0]
    kk = min(n, beam_width)

    result = [('', given_matrix)] # состоит из пар (path: str, matrix: np.ndarray), где path - путь по CNOT-ам до нее
    # по результатам обработки каждого уровня (kn(n-1) матриц) отбираем топ k матриц и обновляем result

    # stop = n ** 3 # заглушка на случай, если что-то пошло не так, чтобы код остановился
    counter = 0
    working = True

    while working:
        counter += 1
        current_top = [(float('inf'), '', np.eye(n, dtype=np.uint8))] * kk # будем использовать кучу для быстрой обработки максимумов, второй элемент в паре путь для данной матрицы
        
        if counter == 1: # обработка начала алгоритма
            k = 1
        else:
            k = kk

        for i in range(k):
            matrix = result[i][1]
            path = result[i][0]
            cnots, matrices = get_neighbours_vectorized(matrix)
            paths = path + cnots
            heuristics = test_heuristic_func.test_heuristic(matrices)
            if np.any(heuristics == 0) and working: # выводим один ответ в красивой форме
                answer = paths[np.where(heuristics == 0)[0]]
                print(' '.join(reversed(textwrap.wrap(answer[0], 2))))
                working = False
                break
            triplets = list(zip(heuristics, matrices, paths))
            top_k = heapq.nsmallest(kk, triplets, key=lambda x: x[0]) # с помощью кучи оставляем только k соседей с наименьшим показателем метрики
            current_top = heapq.nsmallest(kk, top_k + current_top, key=lambda x: x[0]) # обновляем список кандидатов в k лучших матриц на уровне
        result = [(item[2], item[1]) for item in current_top] # обновляем уровень
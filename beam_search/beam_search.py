import numpy as np
import test_heuristic_func
import heapq
from typing import Callable
import heapq
from itertools import count

def get_neighbours_vectorized(matrix): # векторизованный вариант получения соседних вершин с данной
    n = matrix.shape[0]
    cnot_from = []

    for j in range(n):
        cnot_from.append(f"{j}")
    all_neighbors = []
    cnots = []

    for i in range(n):
        cnot_to = [f"{i}"] * n # генерируем заранее известную последовательность cnot-ов
        cnots.append(np.delete((np.array(cnot_from) + np.array(cnot_to)), i))

        base = matrix.reshape((1, n, n))
        additional = np.zeros((n, n, n), dtype=np.uint8)
        additional[:, i, :] = matrix.reshape((n, n))
        all_neighbors.append(np.delete(base ^ additional, i, axis=0))

    return np.concatenate(cnots), np.concatenate(all_neighbors, axis=0)


def beam_search(given_matrix: np.ndarray, beam_width: int, heuristic_func: Callable[[np.ndarray], int]) -> np.ndarray:
    n = given_matrix.shape[0]
    kk = min(n, beam_width)
    unique_id = count() # чтобы не сравнивались матрицы "внутри" кучи


    result = [('', given_matrix)] # состоит из пар (path: str, matrix: np.ndarray), где path - путь по CNOT-ам до нее
    # по результатам обработки каждого уровня (kn(n-1) матриц) отбираем топ k матриц и обновляем result

    stop = n ** 3 # заглушка на случай, если что-то пошло не так, чтобы код остановился
    counter = 0
    working = True

    while working:
        current_top = [(float('-inf'), '', next(unique_id), np.eye(n))] * kk # будем использовать кучу для быстрой обработки максимумов, второй элемент в паре путь для данной матрицы
        
        if len(result) == 1: # обработка начала алгоритма
            k = 1
        else:
            k = kk

        for i in range(k):
            matrix = result[i][1]
            path = result[i][0]
            cnots, matrices = get_neighbours_vectorized(matrix)
            for cnot, matr in zip(cnots, matrices):
                counter += 1 # получаем neighbours этой матрицы, cnot и matr - ребро и вершина соотв
                val = -heuristic_func(matr)
                if val == 0 and working:
                    chars = list(path + cnot) # выводим последовательность cnot
                    for i in range(0, len(chars), 2):
                        chars[i], chars[i+1] = chars[i+1], chars[i]
                    chars = chars[::-1]
                    res = ""
                    for i in range(0, len(chars), 2):
                        res += "".join(chars[i:i+2]) + " "
                    print(f"{res}")
                    working = False
                    break
                elif len(current_top) < k:
                    heapq.heappush(current_top, (val, path + cnot, next(unique_id), matr))
                elif val > current_top[0][0]: # Если текущее число меньше максимума в куче
                    heapq.heapreplace(current_top, (val, path + cnot, next(unique_id), matr))
        result = [(item[1], item[3]) for item in current_top]

m = np.array([[0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1]], dtype=np.uint8)
beam_search(m, 3, test_heuristic_func.test_heuristic)
        
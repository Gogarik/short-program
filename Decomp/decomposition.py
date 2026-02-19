import numpy as np
import json
import math

def Lwr_CNOT_Synth(A, n, m):

    acts = []

    for sec in range(0, math.ceil(n / m)):
        # stage A

        numbers = dict()
        real_m = min(n, sec * m + m) - sec * m

        for row in range(sec * m, n):

            powers_of_two = 1 << np.arange(real_m - 1, -1, -1)
            num = A[row, sec * m : sec * m + real_m].dot(powers_of_two)

            if num == 0:
                continue

            if num not in numbers.keys():
                numbers[num] = []
            numbers[num].append(row)

        for num in numbers.keys():

            for j in range(1, max(len(numbers[num]), 1)):
                row = numbers[num][j]
                A[row] = (A[row] + A[numbers[num][0]]) % 2
                
                acts.append((numbers[num][0], row))

        # stage B and C

        for col in range(sec * m, sec * m + real_m):

            if A[col][col] == 0:
                is_filled = False

                for j in range(col + 1, n):

                    if (A[j][col] == 1 and not is_filled):
                        A[col] = (A[col] + A[j]) % 2
                        acts.append((j, col))

                        is_filled = True
                    
                    if (A[j][col] == 1 and is_filled):
                        A[j] = (A[j] + A[col]) % 2
                        acts.append((col, j))
            else:
                for j in range(col + 1, n):

                    if A[j][col] == 1:
                        A[j] = (A[j] + A[col]) % 2
                        acts.append((col, j))

    return (acts, A)



def CNOT_Synth(matrix, m=None):

    matrix = np.array(matrix)

    if (m is None):
        m = math.ceil(np.log(matrix.shape[0]))
    
    steps1, U = Lwr_CNOT_Synth(matrix, matrix.shape[0], m)
    UT = np.transpose(U)
    steps2, V = Lwr_CNOT_Synth(UT, UT.shape[0], m)

    return (steps1, steps2, matrix.shape[0])
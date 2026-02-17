import decomposition as decomp
import typing as tp

def steps_count(steps1, steps2):

    for i in range(len(steps2)):
        first = steps2[i][0]
        second = steps2[i][1]
        steps2[i] = (second, first)
    
    steps1.reverse()
    steps = steps2 + steps1
    return steps


def visualization(input_file, m=None):
    steps1, steps2, n = decomp.CNOT_Synth(input_file, m)

    steps = steps_count(steps1, steps2)
    for j in range(n):
        for i in range(len(steps) * 2): 

            if (i % 2 != 0):
                print('-', end='')
            else:
                if (j == steps[i // 2][0]):
                    print('o', end='')
                elif (j == steps[i // 2][1]):
                    print('x', end='')
                elif (min(steps[i // 2][0], steps[i // 2][1]) < j < max(steps[i // 2][0], steps[i // 2][1])):
                    print('|', end='')
                else:
                    print('-', end='')
        print()
    
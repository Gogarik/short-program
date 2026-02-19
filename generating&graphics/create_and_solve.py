from generating_random_matrix import *
from generating_avg_CNOTS import *
from generating_by_steps import *
from tqdm import tqdm


def create1():
    n_max = 80
    matrix_count = 50

    for n in range(2, n_max):
        generate_data1(n=n, matrix_count=matrix_count)
    
    generate_avg_CNOTS(n_max=n_max, matrix_count=matrix_count, type='random')

def create2():
    n_max = 50
    matrix_count = 50
    k_max = 80

    for n in tqdm(range(2, n_max)):
        for k in range(1, k_max):
            generate_data2(k=k, matrix_count=matrix_count, n=n)

    generate_avg_CNOTS(n_max=n_max, matrix_count=matrix_count, type='by_step', k_max=k_max)

    
create2()
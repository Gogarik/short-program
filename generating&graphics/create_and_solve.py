from generating_random_matrix import *
from generating_avg_CNOTS import *


def create():
    n_max = 80
    matrix_count = 50

    for n in range(2, n_max):
        generate_data1(n=n, matrix_count=matrix_count)
    
    generate_avg_CNOTS(n_max=n_max, matrix_count=matrix_count)

create()
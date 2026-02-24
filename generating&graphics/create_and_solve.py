import typer
from generating_random_matrix import *
from generating_avg_CNOTS import *
from generating_by_steps import *
from tqdm import tqdm

app = typer.Typer(help="Генерация данных квантовых цепей")

@app.command()
def create1(
    n_max: int = typer.Option(80, "--n-max", "-n", help="Размер матрицы"),
    matrix_count: int = typer.Option(50, "--matrix-count", "-m", help="Количество генерируемых матриц")
):
    """
    Генерация случайных матриц
    """

    for n in range(2, n_max):
        generate_data1(n=n, matrix_count=matrix_count)
    
    generate_avg_CNOTS(n_max=n_max, matrix_count=matrix_count, type='random')

@app.command()
def create2(
    n_max: int = typer.Option(50, "--n-max", "-n", help="Размер матрицы"),
    matrix_count: int = typer.Option(50, "--matrix-count", "-m", help="Количество генерируемых матриц"),
    k_max: int = typer.Option(80, "--k-max", "-k", help="Количество шагов k")
):
    """
    Генерация матриц с помощью шагов
    """
    for n in tqdm(range(2, n_max)):
        for k in range(1, k_max):
            generate_data2(k=k, matrix_count=matrix_count, n=n)

    generate_avg_CNOTS(n_max=n_max, matrix_count=matrix_count, type='by_step', k_max=k_max)


if __name__ == "__main__":
    app()

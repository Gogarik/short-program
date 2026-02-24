from minim_model import *
import typer

app = typer.Typer()

@app.command()
def generate_avg_CNOTS(matrix_count : int = typer.Option(30, '--matrix-count', '-m'),
                       n_max : int = typer.Option(50, '--n-max', '-n')):

    avg_CNOT_counts = np.zeros(n_max, dtype=int)

    folder = '../generating&graphics/random_matrices'

    for n in tqdm(range(2, n_max)):
        link = f'{folder}/matrix({n}x{n})_{matrix_count}.json'

        with open(link, 'r') as f:
            all_matrices = np.array(json.load(f))  # implies all matrices at n by matrix_count

        CNOTS = np.zeros(matrix_count, dtype=int)

        for i in range(matrix_count):
            output = find_min_CNOT_count(all_matrices[i])
            CNOTS[i] = len(output)

        avg_CNOT_counts[n] = np.average(CNOTS)

    with open(f'data_for_graphic4.json', 'w') as f:
        json.dump(avg_CNOT_counts.tolist(), f)

if __name__ == '__main__':
    app()
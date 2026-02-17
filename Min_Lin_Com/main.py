from minim_model import *

def main():
    input_file = 'matrix.json'
    CNOTS = find_min_CNOT_count(input_file)
    print(CNOTS)

if __name__ == "__main__":
    main()
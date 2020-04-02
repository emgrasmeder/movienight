import sys
import numpy as np

def choose(movies):
    return np.random.choice(movies)

def read_csv(file_path):
    with open(file_path, "r") as f:
        return list(map(lambda x: x.strip("\n"), f.readlines()))

def main():
    print(choose(read_csv(sys.argv[1])))

    
if __name__ == "__main__":
    main()

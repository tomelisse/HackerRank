import numpy as np

if __name__ == '__main__':
    shape = tuple(map(int, input().split()))
    print(np.zeros(shape, dtype = np.int))
    print(np.ones(shape, dtype = np.int))

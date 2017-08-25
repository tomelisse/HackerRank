import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = np.array([list(map(int, input().split())) 
                    for _ in range(n)])
    print(arr.mean(axis = 1), arr.var(axis = 0), arr.std(), sep = '\n')


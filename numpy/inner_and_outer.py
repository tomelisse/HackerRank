import numpy as np

if __name__ == '__main__':
    A = np.array(list(map(int, input().split())))
    B = np.array(list(map(int, input().split())))
    print(np.inner(A,B), np.outer(A,B), sep = '\n')

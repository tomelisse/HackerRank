mport numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = np.array([list(map(int, input().split())) 
                        for _ in range(n)])
    print(arr.min(axis = 1).max())

import numpy as np

if __name__ == '__main__':
    n, m, p = list(map(int, input().split()))
    print(np.array([list(map(int, input().split())) 
                    for _ in range(n+m)]))

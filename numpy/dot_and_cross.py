import numpy as np

if __name__ == '__main__':
    n = int(input())
    A = np.array([list(map(int, input().split())) 
                  for _ in range(n)])
    B = np.array([list(map(int, input().split())) 
                  for _ in range(n)])
    print(np.matmul(A,B))

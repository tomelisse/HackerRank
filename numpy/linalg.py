import numpy as np

if __name__ == '__main__':
    print(np.linalg.det(np.array([list(map(float, input().split())) 
                                  for _ in range(int(input()))])))

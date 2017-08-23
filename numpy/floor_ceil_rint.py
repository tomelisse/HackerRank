import numpy as np

if __name__ == '__main__':
    arr = np.array(list(map(float, input().split())))
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))

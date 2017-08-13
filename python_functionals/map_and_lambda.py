cube = lambda x: pow(x, 3) 

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(n-2):
        fib.append(fib[-2] + fib[-1])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

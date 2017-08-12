if __name__ == '__main__':
    n, x     = map(int, input().split())
    marks    = [list(map(float, input().split())) for _ in range(x)]
    students = list(zip(*marks))
    results  = list(map(sum, students))
    results  = [repr(s/float(x)) for s in results]
    print('\n'.join(results))

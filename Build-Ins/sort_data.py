from operator import itemgetter

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    l.sort(key = itemgetter(k))
    print('\n'.join([' '.join([repr(y) for y in x]) for x in l]))

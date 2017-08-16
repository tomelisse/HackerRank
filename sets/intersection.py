if __name__ == '__main__':
    n = int(raw_input())
    A = set(map(int, raw_input().split()))
    m = int(raw_input())
    B = set(map(int, raw_input().split()))
    print len(A & B)

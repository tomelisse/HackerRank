if __name__ == "__main__":
    A = set(map(int, raw_input().split())); N = int(raw_input())
    # number of sets for which A is a strict superset
    k = 0
    for i in range(N):
        B = set(map(int, raw_input().split()))
        if A&B == B and len(A) > len(B):
            k += 1
    print k == N

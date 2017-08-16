m = int(raw_input())
M = set(map(int, raw_input().split()))
n = int(raw_input())
N = set(map(int, raw_input().split()))

sym_dif = (M.difference(N)).union(N.difference(M))
sym_dif = list(sym_dif)
sym_dif.sort()
for i in sym_dif:
    print i

if __name__ == "__main__":
    K = int(raw_input())
    A = map(int, raw_input().split())
    B = set(A)           
    # remove one copy of each room numer from the list
    for i in B:
        A.remove(i)
        if i not in A:
            print i
            break

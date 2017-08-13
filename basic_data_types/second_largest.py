if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    mx = max(arr)
    while mx in arr:
        arr.remove(mx)
    print max(arr)

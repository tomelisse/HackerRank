import datetime as dt

if __name__ == '__main__':
    for _ in range(int(input())):
        t1 = dt.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = dt.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        print(int(abs(dt.timedelta.total_seconds(t1 - t2))))

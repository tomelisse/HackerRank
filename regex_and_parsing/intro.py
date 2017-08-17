import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(bool(re.match('(\+|\-)?\d*\.\d+$', input())))

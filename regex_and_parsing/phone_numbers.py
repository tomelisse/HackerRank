import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print('YES') if bool(re.fullmatch('[789]\d{9}', input())) else print('NO')

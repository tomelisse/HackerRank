import re

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    text = ''.join([''.join(column) 
                    for column in zip(*[input().ljust(m)
                                        for _ in range(n)])])
    print(re.sub(r'(?<=[a-zA-Z0-9])[!@#$%& ]+(?=[a-zA-Z0-9])', ' ', text)

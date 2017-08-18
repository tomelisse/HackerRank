import re

if __name__ == '__main__':
    reg = '[,/.]+'
    l = re.split(reg, input().strip(reg))
    print(*l, sep = '\n')

import re

if __name__ == '__main__':
    reg = '(?<!^)\#(?:[a-f\d]{3}){1,2}'
    for _ in range(int(input())):
        matches = re.findall(reg, input(), re.I)
        if len(matches) != 0:
            print(*matches, sep = '\n')

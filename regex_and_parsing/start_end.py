import re

if __name__ == '__main__':
    s, k = input(), input()
    m = re.finditer(r''+k[0]+'(?='+k[1:]+')', s)
    l = list(map(lambda x: (x.start(), x.start() + len(k) - 1), m))
    print('(-1, -1)') if len(l) == 0 else print(*l, sep = '\n')

import re

if __name__ == '__main__':
    m = re.search(r'([a-zA-Z0-9])\1', input())
    print(m.group(1)) if bool(m) else print(-1)

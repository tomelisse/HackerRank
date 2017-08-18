import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = re.sub('(?<= )\&\&(?= )', 'and', input())
        print(re.sub('(?<= )\|\|(?= )', 'or',s))

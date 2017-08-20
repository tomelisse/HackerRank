import re

def isValid(uid):
    return (bool(re.fullmatch(r'[a-zA-Z0-9]{10}', uid)) 
           and bool(re.search(r'(?:[A-Z].*){2,}', uid))
           and bool(re.search(r'(?:[0-9].*){3,}', uid))
           and not bool(re.search(r'([a-zA-Z0-9]).*\1', uid)))

if __name__ == '__main__':
for _ in range(int(input())):
    print('Valid') if isValid(input()) else print('Invalid')

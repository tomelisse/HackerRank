import re

def isValid(number):
    return (bool(re.match('[4,5,6]', number))
           and bool(re.fullmatch(r'(?:\d{4}-?){3}\d{4}', number))
          and not bool(re.search(r'(\d)(-?\1){3}', number)))

if __name__ == '__main__':
    for _ in range(int(input())):
        print('Valid') if isValid(input()) else print('Invalid')

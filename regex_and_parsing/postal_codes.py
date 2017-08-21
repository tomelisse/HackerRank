import re

if __name__ == '__main__':
    code = input()
    print(bool(re.fullmatch(r'[1-9]\d{5}', code)) 
                    and not bool(re.search(r'(?:(\d)(?=\d\1).*){2}', code)))

from operator import add
from functools import reduce

if __name__ == '__main__':
    text = input()
    text = sorted(text, key = lambda x: (str.isdigit(x), str.isupper(x), 
        str.isdigit(x) and not int(x)%2, x))
    text = reduce(add, text)
    print(text)

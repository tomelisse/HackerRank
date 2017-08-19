from email import utils
import re

def isValid(address):
    return bool(re.fullmatch('[a-z][a-z1-9\._-]*@[a-z]+\.[a-z]{1,3}', address, re.I))

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        text = input()
        name, address = utils.parseaddr(text)
        if isValid(address):
            print(utils.formataddr((name, address)))

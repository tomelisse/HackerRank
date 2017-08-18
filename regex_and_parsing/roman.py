import re

if __name__ == '__main__':
    units     = '(V?I{0,3})|(IV)|(IX)'
    tens      = '(L?X{0,3})|(XL)|(XC)'
    hundreds  = '(D?C{0,3})|(CD)|(CM)'
    thousands = 'M{0,3}'
    print(bool(re.fullmatch(r'('+thousands+')?('+hundreds+')?('+tens+')?('+units+')?', input())))

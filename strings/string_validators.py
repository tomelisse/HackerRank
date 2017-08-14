if __name__ == '__main__':
    string = raw_input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for s in string:
        if s.isalnum():
            alnum = True
        if s.isalpha():
            alpha = True
        if s.isdigit():
            digit = True
        if s.islower():
            lower = True
        if s.isupper():
            upper = True
        if alnum and alpha and digit and lower and upper:
            break
                    
        print alnum
        print alpha
        print digit
        print lower
        print upper

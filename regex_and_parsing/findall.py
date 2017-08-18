import re

if __name__ == '__main__':
    vowels     = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'
    m = re.findall('(?<=['+consonants+'])['+vowels+']{2,}(?=['+consonants+'])', input(), re.I)
    print(*m, sep = '\n') if len(m) else print(-1)

import string
import textwrap
# 'abc...' -> ['a','b','c'...]
letters = textwrap.wrap(string.ascii_lowercase, 1)    
    
def print_line(N, i):
    width = 4*N - 3
    left  = letters[N-1:N-i:-1]
    right = letters[N-i+1:N:1]
    line  = left + [letters[N-i]] + right
    line = '-'.join(line)
    print line.center(width,'-')
            
def print_rangoli(N):
    # upper triangle
    for i in range(1,N+1):
        print_line(N, i)
    # lower triange
    for i in range(N-1,0,-1):
        print_line(N, i)

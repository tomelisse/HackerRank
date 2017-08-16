def s_pop(s, _):
    s.pop()
            
def s_remove(s, number):
    s.remove(int(number))
        
def s_discard(s,number):
    s.discard(int(number))

if __name__=='__main__':
    n = input()
    s = set(map(int, raw_input().split()))
    m = input()
    functions = {'pop':s_pop, 'remove': s_remove, 'discard': s_discard}
    for i in range(m):
        # *number - opctional variable
        command, *number = raw_input().split()
        functions[command](s, number)
        print sum(s)

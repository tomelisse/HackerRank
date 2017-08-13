def insert(l, numbers):
    where = int(numbers[0])
    what  = int(numbers[1])
    l.insert(where, what)
        
def show(l, _) :
    print(l)
        
def remove(l, numbers):
    l.remove(int(numbers[0]))
        
def append(l, numbers):
    l.append(int(numbers[0]))
                 
def sort(l, _):
    l.sort()
                  
def pop(l, _):
    l.pop()
      
def reverse(l, _):
    l.reverse()

if __name__ == '__main__':
    N = int(input())
    l = []
    functions = {'insert':insert, 'print':show,
            'remove':remove, 'append':append, 
            'sort':sort, 'pop':pop, 'reverse':reverse}
    for _ in range(N):
        command, *numbers = input().split()
        functions[command](l, numbers)

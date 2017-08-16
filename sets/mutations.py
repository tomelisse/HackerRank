def update(A, B):
    A|=B
        
def intersection_update(A, B):
    A&=B

def difference_update(A, B):
    A-=B
        
def symmetric_difference_update(A, B):
    A^=B

if __name__ == '__main__':
    n = int(raw_input())
    A = set(map(int, raw_input().split()))
    m = int(raw_input())
    functions = {"update":update, "intersection_update": intersection_update,
                "difference_update":difference_update, 
                 "symmetric_difference_update":symmetric_difference_update}
for i in range(m):
    command = raw_input().split()
    B = set(map(int, raw_input().split()))
    functions[command[0]](A, B)
print sum(A)

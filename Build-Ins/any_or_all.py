def is_palindromic(number):
    ''' checks if the number is palindromic '''
    m = len(number)
    return(all([(number[i] == number[m-i-1]) 
        for i in range(int(m/2))]))
        
if __name__ == '__main__':
    n = int(input()); l = input().split()
    print(all([int(x)>0 for x in l]) 
            and any([is_palindromic(x) for x in l]))

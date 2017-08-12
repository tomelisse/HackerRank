if __name__ == '__main__':
    n = int(raw_input())
    if(n%2 == 0):
        if((n > 1 and n < 6) or (n > 20)):
            print "Not Weird"
        else:
            print "Weird"
    else:
                print "Weird"

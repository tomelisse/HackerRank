def count_substring(string, sub_string):
    # number of sub_strings
    n = 0
    s = string
    # while s contains the sub_string
    while(s.find(sub_string) != -1):
        n = n+1
        where = s.find(sub_string)
        s = s[where+1:]
                
    return n

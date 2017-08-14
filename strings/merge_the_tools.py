import textwrap

def reduce(t):
    u = []
    for i in t:
        if i not in u:
            u.append(i)
    return ''.join(u)

def merge_the_tools(string, k):
    parts = textwrap.wrap(string, k)
    for t in parts:
        print reduce(t)

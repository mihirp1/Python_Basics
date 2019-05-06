import re

def pr(first,second):
    pattern = re.compile(second)
    m = pattern.search(first)
    #print(m.start())
    #print(m.start())
    #print(m.end())
    if not m :
        print("(-1, -1)")
        
    while(m):
        print ("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(first,m.start() + 1)



if (__name__ == "__main__"):
    first = input()
    second = input()
    pr(first,second)
    #print(first,second)

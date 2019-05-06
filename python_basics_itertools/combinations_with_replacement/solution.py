from itertools import combinations_with_replacement

def perm():
 S, n = input().split(" ")
 n  = int(n)
 S  = str(S)
 list_s = list(S)
 list_s.sort()
 length = len(S)
 fin_list = []

 new = list(combinations_with_replacement(list_s,n))
 fin_list.append(new)
 #print(new)

 for element in fin_list:
    for small in element:
        print("".join(small))

 #print(fin_list) 

perm()

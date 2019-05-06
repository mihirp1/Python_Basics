from itertools import combinations

def perm():
 S, n = input().split(" ")
 n  = int(n)
 S  = str(S)
 list_s = list(S)
 list_s.sort()
 length = len(S)
 fin_list = []
 for i in range(1,n+1):
    new = list(combinations(list_s,i))
    fin_list.append(new)
    #print(new)

 for element in fin_list:
    for small in element:
        print("".join(small))
  
 #print(fin_list) 

perm()


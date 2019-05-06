from itertools import permutations

def perm():
 S, n = input().split(" ")
 n  = int(n)
 S  = str(S) 
 list_s = list(S)
 list_s.sort()   

 new = list(permutations(list_s,n))
    
 for element in new:     
    print("".join(element))
    string = []
    
perm()

from itertools import combinations
def prob():
    N = int(input())
    S = list(input().split(" "))
    k = int(input())
    count = 0
    count_list = []
    #print(list(combinations(S,k)))
    X = len(list(combinations(S,k)))
    for A in list(combinations(S,k)):
      "".join(A)
      if ('a' in A):
        count += 1
    p = count
    print(p/X)
    
prob()

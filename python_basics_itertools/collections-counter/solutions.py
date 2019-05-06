from collections import Counter

def countsh():
   X = int(input()) 
   N = list(map(int,list(input().split(" "))))
   counter_dict = Counter(N)
   #print(counter_dict) 
   cust_n = int(input()) 
   i = 0 
   my_list = []
   while(i < cust_n): 
    a, b = list(map(int, list(input().split(" "))))
    if(a in N):
     my_list.append([a,b])
    i = i +1
   sum = 0
    
   for element in my_list:
    if(counter_dict[element[0]] is not 0):
         counter_dict[element[0]] = (counter_dict[element[0]] - 1)
         sum = sum + element[1]
         #print(element[0])
   print(sum)
   #print(counter_dict)         
   #print(my_list)
if __name__ == "__main__":
    countsh()

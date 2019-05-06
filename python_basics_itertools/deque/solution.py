from collections import deque
def deq():
    main_list = []
    d = deque()
    N = int(input())
    i = 0
    while(i<N):
        
        in1 = input()
        #print(a,b)
        main_list.append(in1)
        i = i + 1
    #print(main_list)
    for I in main_list:
        #print(len(I))
        #a,b = I.split(" ")
        if(len(I.split(" ")) == 2):
            a,b = I.split(" ")
            
            a = str(a)
            b = str(b)
            #print(a,b)
            exp = "d."+a+"("+b+")"
            eval(exp)
            #print(exp)
            
 
        else:
            if(I == 'pop'):
                d.pop()
                #print("popped")
                
            if(I == 'popleft'):
                d.popleft()
                #print("popleft")
    d = list(map(str,list(d)))        
    print(" ".join(d))
        
  

    
deq()

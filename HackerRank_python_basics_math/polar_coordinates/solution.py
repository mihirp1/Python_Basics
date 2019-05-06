import cmath

def complex_number():
    temp = input().split('j')[0]
    #print(temp)
    length = len(temp)
    #print(length)
    
    if(length == 4):
        f = int(temp[0] + temp[1])
        s = int(temp[2] + temp[3])
        
    if(length == 3):
        
     if '+' in temp:
      f = int(temp[0])
      s = int(temp[2])
        
     if '-' in temp:
      f = int(temp[0])
      s = int(temp[1] + temp[2])   
        
    if(length == 6):
      f = int(temp[0] + temp[1] + temp[2])  
      s = int(temp[4] + temp[5])
    f = float(f)
    s = float(s)
    x = complex(f,s)
    print(abs(cmath.sqrt(f*f+s*s)))
    print(cmath.phase(x))
    
complex_number()

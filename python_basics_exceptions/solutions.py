def exc():
    T = int(input())
    i = 0
    while(i < T):
        try:
           a , b = map(str,input().split(" ")) 
           print (int(a)//int(b))
        except Exception as e:
           print ("Error Code:",e)
        i = i + 1



if __name__=="__main__":
    exc()

import numpy

if __name__ == "__main__":
    N , M = map(int,input().split(" "))
    #A = list(map(int,input().split(" ")))
    #B = list(map(int,input().split(" ")))
    first_array = []
    second_array = []
    i = 0
    j = 0
    while(i<N):
        A = list(map(int,(input().split(' '))))
        i = i + 1
        first_array.extend(A)
    j = N
    while(j<(2*N)):
        B = list(map(int,(input().split(' '))))
        j = j + 1
        second_array.extend(B)

    
    
    
    n1 = numpy.array(first_array)
    n2 = numpy.array(second_array)
    #print(N,M)
    
    n1 = numpy.reshape(n1,(N,M))
    n2 = numpy.reshape(n2,(N,M))
   
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)
    print(n1//n2)
    print(n1%n2)
    print(n1**n2)
    
    #print(n1,n2)
    

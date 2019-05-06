import numpy

def concat(first,second,n,m,p):
    numpy_array_1 = numpy.array(first)
    numpy_array_2 = numpy.array(second)
    
    np1 = numpy.reshape(numpy_array_1,(N,P))
    np2 = numpy.reshape(numpy_array_2,(M,P))
    print (numpy.concatenate((np1, np2), axis = 0))
    
    
    #print(np1)
    #print(np2)
if __name__ == "__main__":
    i= 0
    j=0
    N,M,P = map(int,input().split(' ')) 
    first_array = []
    A = []
    second_array = []
    B = []
    while(i<N):
        A = list(map(int,(input().split(' '))))
        i = i + 1
        first_array.extend(A)
    j = N    
    while(j<(M+N)):
        B = list(map(int,(input().split(' '))))
        j = j + 1
        second_array.extend(B)
        
    #print(first_array)
    #print(second_array)
    concat(first_array,second_array,N,M,P)
    

import numpy

def tran(my_array,n,m):
    my_np_array = numpy.array(my_array)
    my_np_array = numpy.reshape(my_np_array,(n,m))
    print(numpy.transpose(my_np_array))
    print(my_np_array.flatten())
    

if __name__ == "__main__":
    N, M = map(int,input().split(" "))
    i=0
    myarray = []
    while(i < N):
        
        myarray.extend(list(map(int,input().split(" "))))

        i = i + 1

    tran(myarray,N,M)

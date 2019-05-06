import numpy


if __name__ == "__main__":
    A = list(map(int,input().split(" ")))
    B = list(map(int,input().split(" ")))
    length = len(A)




    n1 = numpy.array(A)
    n2 = numpy.array(B)
    #print(N,M)

    n1 = numpy.reshape(n1,(1,length))
    n2 = numpy.reshape(n2,(1,length))

    print(int(numpy.inner(n1,n2)))
    print(numpy.outer(n1,n2))
    #print(n1)
    #print(n2)



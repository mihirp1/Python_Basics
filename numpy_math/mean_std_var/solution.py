import numpy


if __name__ == "__main__":
    N , M = map(int,input().split(" "))
    first_array = []
    second_array = []
    i = 0
    j = 0
    while(i<N):
        A = list(map(int,(input().split(' '))))
        i = i + 1
        first_array.extend(A)


    n1 = numpy.array(first_array)

    n1 = numpy.reshape(n1,(N,M))



    print(numpy.mean(n1,axis =1))
    print(numpy.var(n1,axis =0))
    print(numpy.std(n1,axis =None))


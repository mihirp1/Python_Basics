import numpy

if __name__ == "__main__":

    M = int(input())
    N = M
    #A = list(map(int,input().split(" ")))
    #B = list(map(int,input().split(" ")))
    first_array = []
    second_array = []
    i = 0
    j = 0
    while(i<N):
        A = list(map(float,(input().split(' '))))
        i = i + 1
        first_array.extend(A)




    n1 = numpy.array(first_array)

    n1 = numpy.reshape(n1,(N,M))

    ans = numpy.linalg.det(n1)
    ans1 = float(str(round(ans, 2)))
    print ("%.1f" % ans1)


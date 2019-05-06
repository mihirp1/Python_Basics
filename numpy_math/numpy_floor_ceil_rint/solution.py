import numpy

if __name__ == "__main__":
    A = list(map(float,input().split(" ")))
    n1 = numpy.array(A)
    print(numpy.floor(n1))
    print(numpy.ceil(n1))
    print(numpy.rint(n1))


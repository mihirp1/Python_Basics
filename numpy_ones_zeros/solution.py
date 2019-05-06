import numpy

def print_one_zero(array):
    print(numpy.zeros((array), dtype = numpy.int))
    print(numpy.ones((array), dtype = numpy.int))


if __name__ == "__main__":
    
    myarray = []
    myarray.extend(map(int,input().split(" ")))
    #print(myarray)
    print_one_zero(myarray) 

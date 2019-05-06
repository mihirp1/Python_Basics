import numpy

def numpy_array():
    numpy_array = numpy.array(list(map(int,input().split(' '))))
    print(numpy.reshape(numpy_array,(3,3)))
    #print(numpy.reshape(numpy_array,(3,3)))
 

if __name__ == "__main__":
    numpy_array()

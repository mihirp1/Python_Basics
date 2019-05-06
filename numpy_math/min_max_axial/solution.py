import numpy


if __name__ == "__main__":
    i = 0
    A = []
    N = 0
    M = 0
    FLAG = False
    while(FLAG is False):
     try:
      #print("in while")
      A.extend(list(map(int,input().split(" "))))
      if(i==0):
         N = len(A)
      i = i + 1
     
     except:
        EOFError
        FLAG = True
        M = i
    numpy_array_1 = numpy.array(A)
    numpy_array_2 = numpy.reshape(numpy_array_1,(M,N))
    #print(numpy_array_2)
    
    print(numpy.max(numpy.min(numpy_array_2, axis = 1), axis = 0))

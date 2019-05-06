def wrap(string, max_width):
    count = 0
    temp = ''
    element = ''
    list_main = []
    [list_main.append(string[(i*max_width):(i*max_width)+max_width]) for i in range(0,(len(string) -1)//max_width)]
    length = len(string)
    remainder = length % max_width
    list_main.append(string[length - remainder :len(string)])
    for element in list_main:
        temp = temp + element + '\n'
    temp = temp.rstrip()
    return (temp)


    '''
    https://www.hackerrank.com/challenges/text-wrap/problem
    '''

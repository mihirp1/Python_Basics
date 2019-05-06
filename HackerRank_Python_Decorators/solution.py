'''
InEfficient Implementation of Python Decorator Hacker Rank problem : 
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
'''
def wrapper(f):
    def fun(l):
        # complete the function
        number = ''
        length = 0
        num_list = []
        for number in l:
            length = len(number)
            if (length == 10):
               format_num = "+91" + " " +number[0:5] + " " + number[5:10] 
               #print(format_num)
               num_list.append(format_num)
            else:
             if(length == 13):
                format_num = "+91" + " " +number[3:8] + " " + number[8:13] 
                num_list.append(format_num)
                
             if(length == 11):
                format_num = "+91" + " " +number[1:6] + " " + number[6:11] 
                num_list.append(format_num)
            
             if(length  == 12):   
                format_num = "+91" + " " +number[2:7] + " " + number[7:12]
                num_list.append(format_num)
                
        #f = num_list
        return(f(num_list))
        
    return fun
    #fun = wrapper(fun)


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


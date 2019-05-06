'''
Marginally Efficient Implementation of Python Decorator Hacker Rank problem : 
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

            format_num = "+91" + " " +number[-10:-5] + " " + number[-5:] 
            num_list.append(format_num)
                
        return(f(num_list))
        
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



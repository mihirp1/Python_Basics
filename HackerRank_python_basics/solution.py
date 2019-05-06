if __name__ == '__main__':
    parsed = []
    N = int(input().strip())
    #print(N)
    #parsed = list(map(str,input().strip().split(' \n')))
    #print(input())
    text = ''
    line = ''
    command = ''
    printable_list = []
    evaluate_string = ''
    
    while True: 
     try:
        line = input()
     except EOFError:
        break
     parsed.append(line)
    text = '\n'.join(parsed)
    #print(parsed)
    list_name = []
    for command in parsed:
        list_name = command.split(' ')
        if(len(list_name) == 3):
            one, two, three = command.split(' ')            
            
            if (one == 'insert'):
                printable_list.insert(int(two),int(three))        
            
        if(len(list_name) == 2):
            
            one, two  = command.split(' ')
        
            if (one == 'remove'):
                printable_list.remove(int(two))
        
            if (one == 'append'):
                printable_list.append(int(two))
                          
                
        if(len(list_name) == 1):
            
            one = command
            #print(one,two,three)
        
            if (one == 'print'):
                print(printable_list)
        
            if (one == 'sort'):
                printable_list.sort()
        
            if (one == 'reverse'):
                printable_list.reverse()
                
            if (one == 'pop'):
                printable_list.pop()
            

def swap_case(s):
    final_list = []
    temp = ''
    new_element = ''
    one = ''
    for element in s:
        if(element.isalpha()):
            if(element.isupper()):
                element = element.lower()
                #print("in here")
                final_list.append(element)
            
            elif(element.islower()):
                element = element.upper()
                final_list.append(element)
        if(not element.isalpha()):
            final_list.append(element)
            
    for one in final_list:
        temp = temp + one
        
    return temp
    print(temp)
    
#if __name__ == "__main__":
    
    #swap_case(s)
            

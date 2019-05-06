if __name__ == '__main__':
    small_list = []
    main_list = []
    highest = 0
    second_highest = []
    iter1=0
    next_list = []
    last_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        small_list.append(name)
        small_list.append(score)
        main_list.append(small_list)
        small_list = []
        second_highest.append(score)
    
    second_highest_set = set(second_highest)
    length = len(second_highest_set)
    next_list = list(second_highest_set)
    next_list.sort()
    highest = next_list[1]

    for element in main_list:
        if(element[1] == highest):
            last_list.append(element[0])
    last_list.sort()
    
    for one in last_list:
        print(one)
    
    #print(highest)
    
         


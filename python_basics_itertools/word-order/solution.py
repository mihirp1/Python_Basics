from collections import OrderedDict
from collections import Counter
 
def distinct():
    N = int(input())
    i=0
    ordered_dict = OrderedDict()
    main_list = []
    while(i<N):
        line = input()
        #print(line)
        main_list.append(line)
        ordered_dict[line] = i
        i = i + 1
    #print(ordered_dict)
    main_ll = []
    for key,ele in ordered_dict.items():
        main_ll.append(key)
    #print(main_ll)
    counter = Counter(main_list)
    setin   = set(main_list)
    print(len(setin))
    last_list = []
    for I in main_ll:
        last_list.append(counter[I])
    last_list = list(map(str,last_list))
    #" ".join(last_list)
    
    print(" ".join(last_list))
    
distinct()

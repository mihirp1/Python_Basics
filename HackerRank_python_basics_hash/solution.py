import hashlib 
if __name__ == '__main__':
    list_of_integers = []
    n = int(input())
    integer_list = map(int, input().split())
    list_of_integers = tuple(list(integer_list))
    print(hash(list_of_integers))

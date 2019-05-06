if __name__ == '__main__':
    n = int(input())
    length = 0
    list_score = []
    arr = map(int, input().split())
    list_score = list(set(arr))
    list_score.sort()
    length = len(list_score)
    #print(list_score)
    print(list_score[length-2])


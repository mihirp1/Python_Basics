if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    iter1 = ''
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        that_score = sum(scores)/3
        student_marks[name] = that_score
    query_name = input()
    for iter1,element in student_marks.items():
        if(iter1 == query_name):
            number = format(student_marks[iter1],'.2f')
            print(number)
    #print(student_marks)


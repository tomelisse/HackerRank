if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
        
    query_marks = student_marks[query_name]
    average = 0
    for mark in query_marks:
        average = average + mark
    average = format(average/len(query_marks),'.2f')
    print average

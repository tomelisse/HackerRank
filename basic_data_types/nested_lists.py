students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
        
# find the lowest grade
min = min([student[1] for student in students])

# find the 2nd lowest grade
min2 = 100
for student in students:
    if (student[1] < min2 and student[1] > min):
        min2 = student[1]
                
# find the students with the 2nd lowest grade      
students2 = [student[0] for student in students if student[1] == min2]
students2.sort()

for student in students2:
        print student

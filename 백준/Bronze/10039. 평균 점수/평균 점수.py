grade_sum = 0
for i in range(5):
    grade = int(input())
    if grade < 40:
        grade_sum += 40
    else:
        grade_sum += grade
print(int(grade_sum/5))
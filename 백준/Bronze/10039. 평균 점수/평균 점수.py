grade_sum = 0
for i in range(5):
    grade = int(input())
    if grade < 40:
        grade_sum += 40
    else:
        grade_sum += grade
print(grade_sum//5) # 나누기가 아니라 몫으로 하면 int 형변환을 안해도 된다.
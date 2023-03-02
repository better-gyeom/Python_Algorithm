N = int(input())  # 학생 수
students = [0] * N
for n in range(N):
    students[n] = n + 1
# print(students)
number = list(map(int, input().split()))
# print(number)

res = []
for i in range(N):
    s = len(res) - number[i] # 학생이 들어가야 할 자리
    # print(s)
    res.insert(s, students[i]) # insert(i, x) : i 인덱스에 x값을 넣어라
print(*res)
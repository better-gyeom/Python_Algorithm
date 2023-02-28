N, K = map(int,input().split())

grade = [[0] * 2 for _ in range(7)]
for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        grade[Y][S] += 1
    else:
        grade[Y][S] += 1

# print(grade)

cnt = 0
for j in range(1, 7):
    for l in range(2):
        # print(grade[j][l])
        if 0 < grade[j][l] <= K:
            cnt += 1
            # print('cnt', cnt)
        elif grade[j][l] > K:
            cnt = cnt + (grade[j][l] // K) + 1
            # print('cnt',cnt)

print(cnt)
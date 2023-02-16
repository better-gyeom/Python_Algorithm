chess_origin = [1, 1, 2, 2, 2, 8]

chess = list(map(int, input().split()))
res = []

for i in range(6):
    res.append(chess_origin[i] - chess[i])

print(*res)
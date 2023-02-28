grid = [[0] * 1001 for _ in range(1001)]

N = int(input())
cnt = 0
for n in range(N):
    y, x, w, h = map(int, input().split())
    cnt += 1
    # print(cnt)
    for i in range(x, x + h):
        for j in range(y, y + w):
            grid[i][j] = cnt

# for g in grid:
#     print(*g)

for n in range(1, N + 1):
    res = 0
    for g in grid:
        res += g.count(n)
    print(res)

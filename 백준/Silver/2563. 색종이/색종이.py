N = int(input())

board = [[0] * 101 for _ in range(101)] # 도화지


for n in range(N):
    a, b = map(int, input().split())
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            board[i][j] = 1

cnt = 0
for b in board:
    # print(*b)
    cnt += b.count(1)
print(cnt)
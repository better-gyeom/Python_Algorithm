T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 30)] * 15 + [[0] * 15 + list(map(int, input().split())) + [0] * 15 for _ in range(N)] + [[0] * (N + 30)] * 15
    # for a in arr:
    #     print(*a)

    delta4 = ((-1, 0), (0, 1), (1, 0), (0, -1))
    delta8 = ((-1, -1), (-1, 1), (1, 1), (1, -1))
    res = []
    for i in range(15, 15 + N):
        for j in range(15, 15 + N):
            fly1 = 0
            for dx, dy in delta4:
                for mul in range(1, M):
                    si = i + dx * mul
                    sj = j + dy * mul
                    fly1 += arr[si][sj]
            res.append(fly1 + arr[i][j])
    # print(res)
    for i in range(15, N + 15):
        for j in range(15, N + 15):
            fly2 = 0
            for dx, dy in delta8:
                for mul in range(1, M):
                    fly2 += arr[i+dx*mul][j+dy*mul]
            res.append(fly2 + arr[i][j])
    # print(res)

    print(f'#{tc} {max(res)}')
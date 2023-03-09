delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(arr, i, j):
    q = [(i, j)]
    arr[i][j] = 0
    cnt = 1

    while q:
        si, sj = q.pop(0)
        for dx, dy in delta:
            if 0 <= si + dx < N and 0 <= sj + dy < N:
                if arr[si + dx][sj + dy] == 1:
                    cnt += 1
                    q.append((si + dx, sj + dy))
                    arr[si + dx][sj + dy] = 0

    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            all = bfs(arr, i, j)
            res.append(all)

res.sort()
print(len(res))
for r in res:
    print(r)

N, M = map(int, input().split())
arr = [0] * (N + 1)
for n in range(N + 1):
    arr[n] = n

for m in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*arr[1:])
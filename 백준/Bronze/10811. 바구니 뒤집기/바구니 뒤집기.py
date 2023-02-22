N, M = map(int, input().split())
arr = [0] * (N + 1)
for n in range(N + 1):
    arr[n] = n
# print(arr)
for m in range(M):
    i, j = map(int, input().split())
    arr[i:j + 1] = reversed(arr[i: j + 1])

print(*arr[1:])
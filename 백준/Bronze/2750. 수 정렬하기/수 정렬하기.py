N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = int(input())

arr.sort()

for j in arr:
    print(j)
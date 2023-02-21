N = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0
for l in lst:
    if l == v:
        cnt += 1

print(cnt)
N , X = map(int,input().split())
lst = list(map(int, input().split()))
A = []
for l in lst:
    if l < X:
        A.append(l)

print(*A)
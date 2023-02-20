X = int(input())
N = int(input())

lst = [0] * N
for i in range(N):
    price, nums = map(int, input().split())
    lst[i] = price * nums

sumnum = 0
for l in lst:
    sumnum += l

if sumnum == X:
    print('Yes')
else:
    print('No')
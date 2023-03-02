N = int(input())

lst = [0] * (N - 1)
me = int(input())
for n in range(N - 1):
    lst[n] = int(input())

# print(me, lst)
cnt = 0
if N == 1:
    print(0)
elif max(lst) - me == 0:
    print(1)
else:
    while True:
        if max(lst) < me:
            print(cnt)
            break
        else:
            me += 1
            buy = lst.index(max(lst))
            lst[buy] -= 1
            cnt += 1
        # print(lst)

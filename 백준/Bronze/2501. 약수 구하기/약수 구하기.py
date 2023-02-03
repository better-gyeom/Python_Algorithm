N, m = map(int,input().split())

# 약수 푸
lst = set()
for i in range(1, N//2):
    if N%i == 0:
        lst.update([i, N//i])
s_lst = sorted(lst)

try:
    print(s_lst[m-1])
except:
    print(0)
    
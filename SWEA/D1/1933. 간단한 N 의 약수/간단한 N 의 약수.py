num = int(input())

num_lst = []
for n in range(1, num // 2 + 1):
    if num % n == 0:
        num_lst.append(int(num / n))
num_lst.append(1)
num_lst.sort()

for i in num_lst:
    print(i, end=' ')
import sys

num_lst = []
for _ in range(1,10):
    num = int(sys.stdin.readline())
    num_lst.append(num)
max_num = max(num_lst)
print(max_num, num_lst.index(max_num)+1, sep='\n')
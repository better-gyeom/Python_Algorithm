import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num = str(A*B*C)
# b = int(input()) * int(input()) * int(input())
# 이렇게도 쓸 수 있구나 !!!!!!!

for n in range(10):
    print(num.count(str(n)))
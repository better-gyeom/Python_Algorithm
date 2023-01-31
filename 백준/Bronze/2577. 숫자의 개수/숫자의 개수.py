import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num = str(A*B*C)
print(num.count('0'))
for n in range(1,10):
    print(num.count(str(n)))
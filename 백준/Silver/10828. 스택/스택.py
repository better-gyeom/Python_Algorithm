import sys

stack = []

for _ in range(int(sys.stdin.readline())):
    char = sys.stdin.readline().split()

    if char[0] == 'push':
        stack.append(char[1])
    elif char[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif char[0] == 'size':
        print(len(stack))
    elif char[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif char[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

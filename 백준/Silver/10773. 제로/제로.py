stack = []
for i in range(int(input())):
    N = int(input())

    if N != 0:
        stack.append(N)
        # print(stack)
    elif N == 0:
        stack.pop()
        # print(stack)

print(sum(stack))
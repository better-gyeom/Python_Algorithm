S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for a in alpha:
    if a in S:
        print(S.index(a), end=' ')
    else:
        print(-1, end=' ')
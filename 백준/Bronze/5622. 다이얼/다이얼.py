dial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
char = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '']

word = input()
res = 0

for w in word:
    for i in range(len(char)):
        if w in char[i]:
            # print(char[i], dial[i])
            res += dial[i]

print(res)
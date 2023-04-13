while True:
    char = list(map(str, input()))
    if char == ['#']:
        break
    else:
        res = 0
        moum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for m in moum:
            res += char.count(m)

        print(res)
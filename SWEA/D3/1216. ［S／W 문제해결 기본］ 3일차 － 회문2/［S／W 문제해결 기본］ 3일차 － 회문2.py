def palin(arr):
    for j in range(100, 0, -1): # 단어길이
        for i in range(100): # 행
            for k in range(100 - j + 1): # 열
                if arr[i][k:k + j] == arr[i][k:k + j][::-1]:
                    return j
    return 0

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    tmp = ''
    arr_t = []
    for i in range(100):
        for j in range(100):
            tmp += arr[j][i]
        arr_t.append(tmp)
        tmp = ''

    if palin(arr) > palin(arr_t):
        print(f'#{tc} {palin(arr)}')
    else:
        print(f'#{tc} {palin(arr_t)}')
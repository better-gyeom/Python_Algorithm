T = int(input())

for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    # arr_t = list(zip(*arr))
    ans = ''
    # for lst in arr_t:
    #     ans += ''.join(lst)

    for j in range(15):
        for i in range(5):
            if j < len(arr[i]): #
                ans += arr[i][j]
    print(f'#{tc} {ans}')
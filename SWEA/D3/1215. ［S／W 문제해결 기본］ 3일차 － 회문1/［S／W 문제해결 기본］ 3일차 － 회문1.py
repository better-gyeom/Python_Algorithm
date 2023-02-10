for tc in range(1, 11):
    T = int(input()) # 찾아야 하는 회문의 길이

    arr = [list(map(str, input())) for _ in range(8)]

    cnt = 0

    # 가로 회문
    for i in range(8):
        for j in range(8 - T + 1):
            if arr[i][j:j+T] == arr[i][j:j+T][::-1]:
                cnt += 1
                # print(arr[i][j:j+T], arr[i][j:j+T][::-1])
    # print(cnt)

    # 세로 회문문
    h_str = ''
    h_arr = []
    for k in range(8):
        for l in range(8 - T + 1):
            for s in range(T):
                h_str += arr[l+s][k]
            h_arr.append(h_str)
            h_str = ''
    for a in h_arr:
        if a == a[::-1]:
            cnt += 1
    print(f'#{tc} {cnt}')
def max_value(lst):
    max_v = lst[0]
    for l in lst:
        if max_v < l:
            max_v = l
    return max_v

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 각 행의 합
    max_width = 0 # 가로 합 중 최댓값을 구할 변수
    width_sum_lst = [] # 가로 합을 모두 저장할 배열
    for i in range(100):
        width_sum = 0 # 가로 합을 넣을 변수
        for j in range(100):
            width_sum += arr[i][j] # 가로 한줄의 합
        width_sum_lst.append(width_sum)
    max_width = max_value(width_sum_lst) # 가로 합들 중 최댓값
    #또는
    # res = 0
    #     if res < tmp:
    #         res = tmp

    # 각 열의 합
    max_height = 0  # 세로 합 중 최댓값을 구할 변수
    height_sum_lst = []  # 세로 합을 모두 저장할 배열
    for j in range(100):
        height_sum = 0  # 세로 합을 넣을 변수
        for i in range(100):
            height_sum += arr[i][j]  # 세로 한줄의 합
        height_sum_lst.append(height_sum)
    max_height = max_value(height_sum_lst) # 세로 합들 중 최댓값

    # 각 대각선의 합
    dia_sum = 0
    dia_sum_r = 0
    for i in range(100):
        dia_sum += arr[i][i]
        dia_sum_r += arr[i][99-i]

    res = [max_width, max_height, dia_sum, dia_sum_r]
    print(f'#{T} {max_value(res)}')
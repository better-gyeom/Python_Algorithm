for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    val = 0
    for i in range(100):
        if arr[99][i] == 2:
            val = i # 2가 있던 열 인덱스 저장
            break
    idx = 99
    while idx > 0:
        if val - 1 >= 0 and  arr[idx][val - 1] == 1: # 왼쪽으로 간 열이 범위 안에 있고, 그 수가 또 1이면
            while val - 1 >= 0 and  arr[idx][val - 1] == 1: # 그 조건을 만족하는 동안은
                val = val - 1 # 계속 빼면서 이동
            idx -= 1 # 왼쪽으로 다 가면 위로 이동
        elif val + 1 < 100 and arr[idx][val + 1] == 1: # 만약 왼쪽 아니고 오른쪽에 1이 있다면
            while val + 1 < 100 and  arr[idx][val + 1] == 1: # 그 조건을 만족하는 동안은
                val = val + 1 # 계속 더하면서 이동
            idx -= 1 # 오른쪽으로 다 가면 위로 이동
        else: # 만약 좌우에 1이 없다면
            idx -= 1 # 그냥 위로 이동

    print(f'#{tc} {val}')
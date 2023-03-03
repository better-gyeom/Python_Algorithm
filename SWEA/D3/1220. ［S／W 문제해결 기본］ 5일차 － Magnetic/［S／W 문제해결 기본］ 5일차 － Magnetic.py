for tc in range(1, 11):
    T = int(input())
    table = [list(map(int, input().split())) for _ in range(T)]
    cnt = 0
    for i in range(T): #세로로 배열을 순회할 것
        state = 0 # 그렇기 때문에 여기에서 초기화
        for j in range(T):
            if table[j][i] == 1 and not state: # 만약에 1을 만났고 상태가 0이면
                state = 1 # 1로 바꾸고
            elif table[j][i] == 2 and state: # 2를 만났는데 상태가 1이면 앞에 1이 있다는 뜻이므로
                cnt += 1 # 하나의 교착상태가 생긴거니까 cnt 증가해주고
                state = 0 # 다시 초기화
    print(f'#{tc} {cnt}')
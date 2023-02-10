for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 스도쿠를 받고
    arr_t = list(zip(*arr)) # 전치행렬을 이용해 스도쿠의 열 확인할 것

    res = 1  # (위의 모든 조건을 통과했다면 스도쿠 성공이므로 1 <- 이건 함수일때라서 맨 밑에 썼는데)
    # 함수를 안쓰고 할거면 우선 참이라는 전제 하에 틀린 것들을 이용해 값을 변경해야함

    for a in arr: # 스도쿠의 한 행씩 돌면서
        if len(set(a)) != 9: # 행을 set 형태로 바꾸어 (중복제거) 전체 길이가 9가 아닌지 확인한다.
            res = 0 # 아니라면 스도쿠 탈락이므로 0

    for a in arr_t: # 스도쿠의 한 열씩 돌면서
        if len(set(a)) != 9: # 위와 동일
            res = 0

    for i in (0, 3, 6): # 스도쿠안을 3*3의 격자로 나누어 확인할 것. 각 격자의 첫 행 인덱스 0, 3, 6
        for j in (0, 3, 6): # 각 격자의 첫 열 인덱스 0, 3, 6
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3] # 슬라이싱을 이용해 3개씩 3번 묶어 하나의 배열 만들어
            if len(set(lst)) != 9: # 또 set 형태로 바꾸어 전체길이가 9가 아닌지 확인
                res = 0 # 아니라면 스도쿠 탈락

    print(f'#{tc} {res}')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # print(flag)

    mx = 0 # 최대한 많은 국기를 갖고 있어야 칠할 횟수가 적어지므로 최대한 많은 국기의 개수를 저장할 변수
    for i in range(N - 2): # 'W'로 색칠될 줄의 영역
        for j in range(i + 1, N - 1): # 'B'로 색칠될 줄의 영역
            cnt = 0 # 색칠을 한 각 경우마다 초기화 해줘야 하니까 위치가 여기
            for s in range(i + 1): # 'W' 개수 세기
                cnt += flag[s].count('W')
            for s in range(i + 1, j + 1): # 'B' 개수 세기
                cnt += flag[s].count('B')
            for s in range(j + 1, N): # 'R' 개수 세기
                cnt += flag[s].count('R')
            mx = max(mx, cnt) # 그 전 과정의 국기 개수와 현재 내가 센 국기 개수 중 큰값 넣기
    res = (N * M) - mx # 바꿔야 할 국기는 전체에서 기존 국기를 빼는 것

    print(f'#{tc} {res}')

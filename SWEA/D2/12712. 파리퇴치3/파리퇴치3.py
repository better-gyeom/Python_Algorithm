T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    # 인덱스 오류가 나지 않게 패딩을 붙였다.
    arr = [[0] * (N + 30)] * 15 + [[0] * 15 + list(map(int, input().split())) + [0] * 15 for _ in range(N)] + [[0] * (N + 30)] * 15
    
    # for a in arr:
    #     print(*a)
    res = [] # 각 자리에 스프레이를 뿌릴 때마다 잡히는 파리의 개수를 담을 배열

    delta4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 4방향 먼저 확인

    for i in range(15, 15 + N): # 패딩을 제외한 값만 확인
        for j in range(15, 15 + N):
            fly1 = 0
            for dx, dy in delta4: # 4방향을 탐색하며
                for mul in range(1, M): # 스프레이의 범위만큼 나아가기
                    fly1 += arr[i + dx * mul][j + dy * mul] # 확인하며 값을 더해주기
                    
            res.append(fly1 + arr[i][j]) # 4방향으로 모두 더한 값을 res 에 저장하기
    # print(res)

    delta8 = ((-1, -1), (-1, 1), (1, 1), (1, -1)) # 8방향도 확인

    for i in range(15, N + 15):
        for j in range(15, N + 15):
            fly2 = 0
            for dx, dy in delta8:
                for mul in range(1, M):
                    fly2 += arr[i + dx * mul][j + dy * mul]
                    
            res.append(fly2 + arr[i][j])
    # print(res)

    print(f'#{tc} {max(res)}')
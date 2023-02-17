for _ in range(10):
    tc, length = map(int, input().split()) # test case 와 길의 총 개수

    road = list(map(int, input().split())) # 한방향 길 이 주어진 리스트

    arr = [[0] * 100 for _ in range(100)] # 연결된 노드를 표시할 배열
    visited = [False] * 100 # 방문 기록 배열
    stack = []

    for i in range(length):
        arr[road[i * 2]][road[i * 2 + 1]] = 1 # 길이 주어진 리스트에서 2개씩 가져와서 한방향 노드 표시

    v = 0 # A부터 시작
    visited[0] = True # 방문 기록 남기고
    stack.append(v) # stack 에 추가

    res = 0 # 길이 없으면 출력하기 위한 0
    while True:
        if v == 99: # 정점이 99면 도착지점 이라는 뜻이고, 길이 있다는 것이므로
            res = 1 # 1 기록
            break # 찾는 순간 나가버리기

        for w in range(100): # v와 연결된 정점들을 확인하면서
            if arr[v][w] == 1 and visited[w] == False: # 길이 있고, 방문한적이 없으면
                visited[w] = True # 방문해주고
                stack.append(v) # stack 에 기록
                v = w # 정점을 바꿔주고
                break # 나가기
        else: # 다 돌고서 (for-else 문)
            if stack: # 스택에 정점이 남아있으면
                v = stack.pop() # 다시 되돌아가기
            else: # 스택이 비었으면
                break # 종료

    print(f'#{tc} {res}')
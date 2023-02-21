delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y): # 좌표
    q = [(x, y)] # 통째로 큐에 넣기
    while q:
        x, y= q.pop(0) # 첫번째 원소 뽑아서 좌표생성
        for dx, dy in delta: # 델타 탐색
            nx = x + dx # 사방을 좌표 확인
            ny = y + dy # 해주기
            if 0 <= nx < n and 0 <= ny < n: # 4방향의 좌표가 범위 안에 있으면
                if maze[nx][ny] == 0: # 0인지 확인. 통로면
                    maze[x][y] = 1 # 현재 내 자리를 1로 채우기
                    q.append([nx, ny]) # 그리고 0이었던 자리의 좌표 큐에 넣기

                elif maze[nx][ny] == 3: # 또는 3이면. 종료이므로
                    return 1 # 그때의 cnt 출력
    return 0

for tc in range(1, 11):
    t = int(input())
    n = 16
    maze = [list(map(int, input())) for _ in range(16)]
    res = 0

    for x in range(n):
        for y in range(n): # 미로의 좌표값을 하나씩 확인하다가
            if maze[x][y] == 2: # 2가 보이면 출발점이므로
                res = bfs(x, y) # 그 좌표를 가지고 함수 시작

    print(f'#{tc} {res}')
T = int(input()) # 컴퓨터의 수

arr = [[0] * (T + 1) for _ in range(T + 1)] # 노드(연결된 컴퓨터)가 입력될 2차원 배열
visited = [False] * (T + 1) # 방문여부 배열
stack = [] # 탐색 길 기록할 배열

for i in range(int(input())): # 컴퓨터 쌍의 수 만큼 돌면서 노드 입력받기
    a, b = map(int, input().split()) # 연결된 컴퓨터
    arr[a][b] = 1
    arr[b][a] = 1

cnt = 0
v = 1 # 시작 지점
visited[v] = True # 방문 기록
stack.append(v) # 길 기록

while True:
    for w in range(T + 1):
        if arr[v][w] and not visited[w]: # 1이고 (연결되어있고) 방문한적 없으면
            visited[w] = True # 방문 기록 남기고
            # v = w # 메인을 바꾸고
            cnt += 1
            stack.append(w) # 스택에 추가 (길 기록)
            break
    else: # 위에 다 돌고서
        if stack: # stack 이 비어있지 않으면
            v = stack.pop() # 되돌아가 ! 가서 다시 탐색해 빼놓은거 없나
        else: # 비어있으면 다 탐색한거지
            break # 나가자

print(cnt)
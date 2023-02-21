def dfs(graph, snode, c): # 그래프, 시작정점, 정점의 개수
    visited = [False] * (c + 1) # 방문배열
    stack = [] 
    res = []

    start = snode # 시작 정점 정하고
    visited[start] = True # 시작 정점은 방문했으니까 방문 표시
    res.append(start) # 과정 표시

    while True:
        for w in range(c + 1): # 그래프를 돌면서
            if graph[start][w] and not visited[w]: # 그래프의 값이 1이고 방문하지 않았으면
                stack.append(start) 
                start = w # 시작 정점 바꿔주기
                visited[w] = True # 방문기록 남겨주고
                res.append(w) # 과정 표시
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    return res

def bfs(graph, snode, c): # 그래프, 시작 정점, 정점의 개수
    visited = [0] * (c + 1)
    q = [snode]
    visited[snode] = 1
    res = []
    
    while q:
        t = q.pop(0)
        res.append(t)
        graph[t].sort()
        for idx in graph[t]:
            if not visited[idx]:
                q.append(idx)
                visited[idx] = visited[t] + 1
    return res


N, M, V = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
arr = [[0] * (N + 1) for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)
    arr[a][b] = 1
    arr[b][a] = 1
# print(adjL)
# print(arr)
d = dfs(arr, V, N)
b = bfs(adjL, V, N)

print(*d)
print(*b)

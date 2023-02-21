def bfs(graph, snode): # 그래프, 시작정점, 정점의 개수
    visited = [0] * 101
    q = [snode]
    res = []
    visited[snode] = 1

    while q:
        t = q.pop(0)
        # print(t)
        # res.append(t)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    return visited


for tc in range(1, 11):
    long, snode = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)
    adjL = [[] for _ in range(101)]

    for i in range(long // 2):
        a = lst[i * 2]
        b = lst[i * 2 + 1]
        adjL[a].append(b)

    # print(adjL)
    res = bfs(adjL, snode)
    # print(res)
    mx = res[0]
    for idx in range(len(res)):
        if mx <= res[idx]:
            mx = res[idx]
            mx_idx = idx

    print(f'#{tc} {mx_idx}')
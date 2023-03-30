
def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N): # 길이만큼 돌면서
        if v[j] == 0: # 방문하지 않았으면
            v[j] = 1 # 방문 기록 남기고
            dfs(n + 1, sm + arr[n][j]) # 그 다음 dfs실행
            v[j] = 0 # 다시 초기화

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N         # 방문 기록 남길 리스트
    ans = 100 * N

    dfs(0, 0)
    print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
    cnt = 0
    res = 'Possible'

    for t in times:
        cnt += 1 # 사람이 한명 올때마다
        if cnt > (t // M) * K: # 붕어빵 개수 확인해서 충족하지 않으면
            res = 'Impossible'
            break

    print(f'#{tc} {res}')
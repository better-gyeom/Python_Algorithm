def power(n, m):
    if m == 1:                      # 횟수가 점점 줄어서 1번이 되면
        return n                    # n을 출력
    else:                           # 횟수가 1이 아닐땐
        return n * power(n, m - 1)  # 거듭제곱 함수 출력하며 n 곱해주기

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    print(f'#{tc} {power(N, M)}')
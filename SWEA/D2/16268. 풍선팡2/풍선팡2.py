T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    # print(balloon)
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

    lst = []
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            flower = 0
            for di, dj in delta:
                flower += balloon[i + di][j + dj]
            lst.append(flower + balloon[i][j])

    # print(lst)
    print(f'#{tc} {max(lst)}')
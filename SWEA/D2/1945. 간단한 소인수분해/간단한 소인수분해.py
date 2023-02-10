T = int(input())

for tc in range(1, T+1):
    N = int(input())

    divs = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(divs)):
        while N % divs[i] == 0:
            cnt[i] += 1
            N = N // divs[i]

    print(f'#{tc}', *cnt)
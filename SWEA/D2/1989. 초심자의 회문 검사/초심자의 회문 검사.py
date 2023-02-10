def len_check(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

T = int(input())

for tc in range(1, T + 1):
    strs = list(map(str, input()))

    N = len_check(strs)

    for i in range(N // 2): # 인덱스를 절반만 돌면서
        if strs[i] == strs[N - 1 - i]: # 끝과 시작을 같은지 비교
            res = 1 # 전부같으면 1
        else: # 하나라도 다르면
            res = 0
    print(f'#{tc} {res}')
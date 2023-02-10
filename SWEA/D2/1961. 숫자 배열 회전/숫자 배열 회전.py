def turnNin(arr, n): # 90도로 돌리는 함수
    res = [] # 90도로 돌린 후 문자열로 묶어서 넣을 배열
    tmp = [[0] * n for _ in range(n)] # 90도로 돌린 배열을 임시로 넣을 곳
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[N-1-j][i] # 90도로 회전시켜 새로운 배열에 넣기
    for n in tmp:
        res.append(''.join(n)) # 배열의 행을 묶기
    return res

for tc in range(1, int(input())+1):
    N = int(input()) # 배열의 크기
    rotation = [list(map(str, input().split())) for _ in range(N)] # 처음 숫자 배열
    ro90 = [[0] * N for _ in range(N)]
    ro180 = [[0] * N for _ in range(N)]
    ro270 = [[0] * N for _ in range(N)]

    ro90 = turnNin(rotation, N) # 90도 돌린 것
    ro180 = turnNin(ro90, N) # 180도 돌린 것
    ro270 = turnNin(ro180, N) # 270도 돌린 것

    print(f'#{tc}')
    for a, b, c in zip(ro90, ro180, ro270): # 각각의 리스트의 첫번째 원소, 두번째원소, 세번째 원소들을 묶고
        print(f"{''.join(a)} {''.join(b)} {''.join(c)}") # 보여주기

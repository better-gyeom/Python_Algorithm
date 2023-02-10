def check(arr):
    ans = 0 # 단어가 들어갈 수 있는 갯수 세는 변수
    for i in arr: # 퍼즐칸의 행을 돌면서
        cnt = 0 # 3이 되는 순간을 세기 위한 변수
        for j in i: # 행 안의 숫자를 하나씩 확인하여
            if j == 1: # 1이면
                cnt += 1 # 하나 세기
            else: # 0이면
                if cnt == K: # cnt 가 들어갈 단어의 길이와 같은지 확인. 같으면
                    ans += 1 # 갯수 추가
                cnt = 0 # 아니면 다시 초기화
    return ans

for tc in range(1, int(input())+1):
    N, K = map(int,input().split()) # 퍼즐칸의 크기, 들어갈 단어의 길이

    arr = [list(map(int, input().split()))+ [0] for _ in range(N)] + [[0]*(N+1)] # 기존 퍼즐칸에 오른쪽, 아래 패딩 추가하여 생성
    arr_t = list(map(list, zip(*arr))) # 기존 퍼즐칸을 전치행렬로 뒤집기 (열로 묶기. for 문을 안쓰고 이렇게 할 수도 있음)

    # print(arr)
    # print(arr_t)

    # [1]
    print(f'#{tc} {check(arr) + check(arr_t)}')

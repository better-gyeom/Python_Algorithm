T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 버스 노선의 개수

    cnts = [0] * 5001 # 버스가 도착하는 정류장을 기록하기 위한 전체 정류장

    for _ in range(N): # 노선만큼 반복하면서
        S, E = map(int, input().split()) # 노선의 처음과 끝을 받고
        for i in range(S, E+1): # 노선의 길이만큼
            cnts[i] += 1 # 1 추가

    P = int(input())
    res = [0] * P

    for j in range(P):
        k = int(input())
        res[j] = cnts[k]

    print(f'#{tc}', *res) # res를 list로 써서 append한 다음 *res 해도 된다.
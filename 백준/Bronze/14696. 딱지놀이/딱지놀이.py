N = int(input()) # 총 라운드 개수

for n in range(N): # 각 라운드마다
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = A[1:]
    b = B[1:]
    if a.count(4) == b.count(4):
        if a.count(3) == b.count(3):
            if a.count(2) == b.count(2):
                if a.count(1) == b.count(1):
                    res = 'D'
                else:
                    res = 'A' if a.count(1) > b.count(1) else 'B'
            else:
                res = 'A' if a.count(2) > b.count(2) else 'B'
        else:
            res = 'A' if a.count(3) > b.count(3) else 'B'
    else:
        res = 'A' if a.count(4) > b.count(4) else 'B'

    print(res)
A, B, C = map(int, input().split())

# 시간 초과
# i = 0
# while True:
#     i += 1
#     cost = A + B * i
#     rev = C * i
    
#     if cost < rev: # rev - cost == C * i - (A + B * i) == (C - B) * i - A >= 0
#         print(i)
#         break

# 계산 값 자체로 풀기
# A // (C - B) + 1 == i
if C - B <= 0: # 나누는 수가 0이 될 수는 없으니까...
    print(-1) # 그런 경우는 손익분기점이 생기지 않으니 -1 출력
else:
    print(A // (C - B) + 1)

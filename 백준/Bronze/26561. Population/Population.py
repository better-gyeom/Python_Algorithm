T = int(input())

for i in range(T):
    p, t = map(int, input().split())
    print(p - (t // 7) + (t // 4))

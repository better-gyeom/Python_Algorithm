T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    num = list(map(int,input().split()))
    for idx in num :
        sum += idx
    ave = round(sum / len(num))
    print(f'#{test_case} {ave}')
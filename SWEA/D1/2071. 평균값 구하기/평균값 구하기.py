T = int(input())

for test_case in range(1, T + 1):
    summ = 0
    num = list(map(int,input().split()))
    for idx in num :
        summ += idx
    ave = round(summ / len(num))
    print(f'#{test_case} {ave}')
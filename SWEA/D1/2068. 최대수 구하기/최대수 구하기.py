T = int(input())

for test_case in range(1,T+1) :
    num = list(map(int,input().split()))
    max = num[0]
    for i in range(len(num)) :
        if num[i] > max :
            max = num[i]
    print(f'#{test_case} {max}')
    max = 0
    
        
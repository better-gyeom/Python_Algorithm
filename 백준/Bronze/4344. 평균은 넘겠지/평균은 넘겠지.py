T = int(input())

for tc in range(1, T+1):
    N_nums = list(map(int,input().split()))
    cnt = 0 # 평균을 넘는 학생 수 기록
    ava = sum(N_nums[1:]) / (len(N_nums) - 1)

    for n in N_nums[1:]:
        if n > ava: # 평균보다 높은 점수면
            cnt += 1 # 기록

    res = cnt / (len(N_nums) - 1) * 100
    print(f'{round(res, 3):.3f}%')

test_case = int(input())

for t in range(test_case):
    high, wide, N = map(int, input().split())

    ho = N // high + 1# 번째에서 층으로 나눈 몫 = 호수
    floor = N % high # 번째에서 층으로 나눈 나머지 = 층수
    if floor == 0:
        ho = N // high
        floor = high
    print(f'{floor*100+ho}')
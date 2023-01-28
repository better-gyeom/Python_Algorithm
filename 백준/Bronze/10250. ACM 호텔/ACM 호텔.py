test_case = int(input())

for t in range(test_case):
    high, wide, N = map(int, input().split()) # list로 하지 않아도 변수 세개 생성하면 전부 받을 수 있음

    ho = N // high + 1 # N번째에서 층으로 나눈 몫 = 호수
    floor = N % high # N번째에서 층으로 나눈 나머지 = 층수
    
    if floor == 0: # 만약 나누어 떨어진다면
        ho = N // high # 호수는 1을 더하지 않고
        floor = high # 층수는 나눈 수 그대로가 된다. (이 부분을 쓰지 않아서 계속 틀림)
        
    print(f'{floor*100+ho}')
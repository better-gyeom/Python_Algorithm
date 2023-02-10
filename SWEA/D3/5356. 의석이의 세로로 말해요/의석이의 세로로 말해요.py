T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)] # 문자열 입력받기

    for i in range(5):
        arr[i] += ' ' *(15-len(arr[i])) # 최대 15까지 길이가 된다고 했으니까 기존 문자열의 길이를 제외한 나머지를 공백으로 채움

    strs = ''
    res_arr = []
    for j in range(15):
        for k in range(5):
            if arr[k][j] != ' ': # 공백이 아닌경우에만
                strs += arr[k][j] # 문자열을 세로로 추가하여
        res_arr.append(strs) # 세로로 읽은 문자열 리스트 새로 생성
        strs = ''

    res_arr = [v for v in res_arr if v] # 빈 리스트가 아닌 것만 다시 만들어서
    print(f'#{tc}', end=' ')
    print(*res_arr, sep='') # 띄어쓰기 없이 출력
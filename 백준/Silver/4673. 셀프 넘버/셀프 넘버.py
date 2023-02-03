def fn_d(n): #각 자릿수 숫자들과 자신을 더한 숫자를 구하는 함수
    num = str(n) #문자열로 숫자를 입력 받고
    add = 0
    for i in range(len(num)): #for문으로 반목하면서
        add += int(num[i]) #문자열의 인덱스(즉 각자리 숫자들)을 더해감
    return add + int(n) #각자리 숫자를 더한 값과 자기자신을 반환

def is_selfnumber(m): #셀프넘버를 판별하는 함수
    n_num = set(range(1,m+1)) #원하는 범위의 자연수를 집합으로 생성
    g_num = []
    for i in range(1,m+1): #for문으로 원하는 범위까지 반복하면서
        g_num.append(fn_d(i)) #g_num 리스트에 제너레이터 입력
    g_num = set(g_num)
    return list(n_num - g_num) #차집합을 이용하여 전체 숫자에서 제너레이터 제외

sort_self = sorted(is_selfnumber(10000))
for s in sort_self:
    print(s)#정렬하여 프린트
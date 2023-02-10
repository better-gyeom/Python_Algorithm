for tc in range(1, int(input())+1):
    T, num = input().split()

    lst = list(map(str, input().split()))
    day = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    l_dic = {}
    for l in lst:
        if l not in l_dic:
            l_dic[l] = 1
        else:
            l_dic[l] += 1
    # print(l_dic)

    res = ''
    for d in day:
        if d in l_dic:
            res += (d + ' ') * l_dic[d]

    print(f'#{tc}')
    print(f'{res}')
for i in range(int(input())):
    re, ch= input().split()
    ch_lst = []
    for j in ch:
        ch_lst.append(j*int(re))

    print(''.join(ch_lst))
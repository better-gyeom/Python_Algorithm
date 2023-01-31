test_case = int(input())

for _ in range(test_case):

    ox_lst = input()
    count = 0
    cnt_lst = []

    for ox in ox_lst:
       
        if ox == 'O':
            count +=1
            cnt_lst.append(count)
        else:
            count = 0
    print(sum(cnt_lst))
def solution(s):
    answer = []
    tmp = []
    tuple_lst = []
    tmp_char = ''
    
    for idx in range(1, len(s)-1):
        if s[idx] == '{':
            continue
        elif s[idx] == ',':
            if tmp_char:
                tmp.append(int(tmp_char))
                tmp_char =''
        elif s[idx] == '}':
            tmp.append(int(tmp_char))
            tuple_lst.append(tmp)
            tmp_char = ''
            tmp = []
        else:
            tmp_char += s[idx]
    # print(tuple_lst)
    
    tuple_lst.sort(key=len)
    # print(tuple_lst)
    
    
    for lst in tuple_lst:
        for ls in lst:
            if not ls in answer:
                answer.append(ls)
    return answer
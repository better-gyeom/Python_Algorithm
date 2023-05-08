def change(n, arr):
    change_arr = []
    res = ''
    for i in range(len(arr)):
        for j in range(n - 1, -1, -1):
            if arr[i] & (1 << j):
                res += '#'
                # print(res)
            else:
                res += ' '
                # print(res)
        change_arr.append(res)
        # print(change_arr)
        res = ''
    return change_arr

def solution(n, arr1, arr2):
    answer = []
    res2 = ''
    change_arr1 = change(n, arr1) # arr1 #으로 변경
    change_arr2 = change(n, arr2) # arr2 #으로 변경
    
    for i in range(n):
        for j in range(n):
            if change_arr1[i][j] == '#' or change_arr2[i][j] == '#':
                res2 += '#'
            else:
                res2 += ' '
        answer.append(res2)
        res2 = ''
            
    return answer
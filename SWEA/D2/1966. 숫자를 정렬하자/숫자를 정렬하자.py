def maxPro(arr): # 최댓값 구하는 함수
    maxV = arr[0]
    for a in arr:
        if maxV < a:
            maxV = a
    return maxV

def toString(string): # 숫자 리스트를 문자열로 바꾸는 함수
    res = ''
    for s in string:
        res += str(s) + ' '
    return res

T = int(input()) #test case 개수

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = [0] * int(maxPro(nums) + 1) # (nums의 최대 숫자 +1)개를 갖는 배열
    temp = [0] * N # 새로 정리된 숫자를 받을 배열

    for num in nums:
        cnt[num] += 1 # nums의 수를 확인하고, 그 수로 인덱스를 갖는 곳에 1 추가
    # print(cnt)
    for i in range(1, len(cnt)): # 누적합
        cnt[i] = cnt[i-1] + cnt[i]
    # print(cnt)
    # print(len(nums)-1)
    # print('----------------')
    for i in range(len(nums)-1, -1, -1): # i = 배열의 끝 인덱스부터 하나씩 내려올거야
        cnt[nums[i]] -=  1 # nums[i]번째 값을 인덱스로 갖는 cnt의 값을 하나 줄여준다.
        # print(cnt)
        # print(nums[i])
        temp[cnt[nums[i]]] = nums[i] # 하나 줄인값을 인덱스로 갖는 temp값에 nums[i]넣는다.

    print(f'#{tc} {toString(temp)}')
def max_check(arr):
    max_v = -1e9
    for a in arr:
        if max_v < a:
            max_v = a

    return max_v


def counting_sort(arr):
    cnt = [0] * (max_check(arr) + 1)
    tmp = [0] * len(arr)
    for i in arr:
        cnt[i] += 1  # 기존 배열에 있는 값을 인덱스로 하여 갯수 세기
    for j in range(1, len(cnt)):
        cnt[j] = cnt[j - 1] + cnt[j]  # 누적합으로 만들기
    for k in range(len(arr) - 1, -1, -1):
        cnt[arr[k]] -= 1
        tmp[cnt[arr[k]]] = arr[k]  # 정렬하며 값 새로 집어넣기

    return tmp


for tc in range(1, 11):
    times = int(input())
    boxes = list(map(int, input().split()))
    sort_boxes = counting_sort(boxes)
    for time in range(times):
        sort_boxes[0] += 1
        sort_boxes[-1] -= 1
        sort_boxes = counting_sort(sort_boxes)

    print(f'#{tc} {sort_boxes[-1] - sort_boxes[0]}')

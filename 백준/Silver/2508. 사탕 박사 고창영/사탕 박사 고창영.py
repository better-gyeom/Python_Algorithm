T = int(input())

for tc in range(T):
    blank = input()
    r, c = map(int, input().split())
    candy = [input() for _ in range(r)]
    candy_t = list(map(list, zip(*candy)))

    cnt = 0
    # print(candy_t)
    for i in candy:
        cnt += i.count('>o<')
        # print(cnt)
    for j in candy_t:
        j_t = ''.join(j)
        cnt += j_t.count('vo^')
    print(cnt)
N, M = map(int, input().split())
cards = list(map(int, input().split()))

sum_card = []
for i in range(N):
    for j in range(i, N):
        if i != j:
            for k in range(j, N):
                if i != k and j != k:
                    # print(cards[i], cards[j], cards[k])
                    sum_card.append(cards[i] + cards[j] + cards[k])
sum_card.sort()

res = []
for s in sum_card:
    if s <= M:
        res.append(s)

print(res[-1])
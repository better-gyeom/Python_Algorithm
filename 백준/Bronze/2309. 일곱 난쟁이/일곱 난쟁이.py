nine = []

for n in range(9):
    nine.append(int(input()))

# print(nine)

total = sum(nine)
res = []
fake1 = fake2 = 0
for i in range(9):
    for j in range(9):
        if j != i:
            if total - (nine[i] + nine[j]) == 100:
                fake1, fake2 = i, j

for k in range(9):
    if k != fake1 and k != fake2:
        res.append((nine[k]))

for r in sorted(res):
    print(r)
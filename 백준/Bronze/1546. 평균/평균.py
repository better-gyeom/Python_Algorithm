N = int(input())
grades = list(map(int, input().split()))

res = []
for g in grades:
    res.append(g / max(grades) * 100)

print(sum(res) / N)
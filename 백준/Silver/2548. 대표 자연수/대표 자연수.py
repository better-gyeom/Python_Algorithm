import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

diff = []
nums.sort()
for i in range(N):
    diff_value = 0
    for j in range(N):
        if i != j:
            diff_value += abs(nums[i] - nums[j])
    diff.append(diff_value)

mn = min(diff)
idx = diff.index(mn)
print(nums[idx])

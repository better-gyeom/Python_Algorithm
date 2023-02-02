nums = [0] * 5
for i in range(5):
    nums[i] = int(input())
nums.sort()
print(int(sum(nums)/len(nums)))

if len(nums) % 2 != 0:
    idx = len(nums) // 2
    print(nums[idx])
else:
    idx = len(nums) // 2
    print((nums[idx] + nums[idx+1]) / 2)
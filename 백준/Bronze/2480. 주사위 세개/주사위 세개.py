nums = list(map(int,input().split()))

if nums[0] == nums[1] and nums[1] == nums[2]:
    print(nums[0] * 1000 + 10000)
elif nums[0] == nums[1] and nums[1] != nums[2]:
    print(nums[0] * 100 + 1000)
elif nums[1] == nums[2] and nums[2] != nums[0]:
    print(nums[1] * 100 + 1000)
elif nums[0] == nums[2] and nums[2] != nums[1]:
    print(nums[0] * 100 + 1000)
else:
    print(max(nums) * 100)
num1 = input()
num2 = input()
num_list = []

for n in num2:
    num_list.append(int(num1) * int(n))
num_list.reverse()
for nums in num_list:
    print(nums)
print(int(num1)*int(num2))

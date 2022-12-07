file = open("input.txt")

nums = []
for line in file:
    nums.append(int(line))

changes = [nums[i]-nums[i-1] for i in range(1, len(nums))]
print(sum([1 for num in changes if num > 0]))

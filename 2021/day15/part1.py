file = open("input.txt")

nums = []

for line in file:
    nums.append([int(x) for x in list(line.strip())])

for col in range(1, len(nums[0])):
    nums[0][col] += nums[0][col-1]
for row in range(1, len(nums)):
    nums[row][0] += nums[row-1][0]

for row in range(1, len(nums)):
    for col in range(1, len(nums[0])):
        less = min(nums[row-1][col], nums[row][col-1])
        nums[row][col] += less

print(nums[-1][-1] - nums[0][0])

file = open("input.txt")

nums = []
for line in file:
    nums.append(int(line))

slides = [nums[i]+nums[i+1]+nums[i+2] for i in range(len(nums) - 2)]
changes = [slides[i]-slides[i-1] for i in range(1, len(slides))]
print(sum([1 for num in changes if num > 0]))

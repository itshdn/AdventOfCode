def calc(lst):
    res = 0
    for idx in range(len(lst)):
        res += lst[idx] * 2**(len(lst) - (idx + 1))
    return res


file = open("input.txt")

nums = []
for line in file:
    nums.append([int(x) for x in list(line.strip())])

cur = nums[0]
for idx in range(1, len(nums)):
    cur = [nums[idx][i] + cur[i] for i in range(len(cur))]

gamma, epsilon = [], []

for num in cur:
    if num == len(nums) // 2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(num > len(nums)//2)
        epsilon.append(num < len(nums)//2)

print(calc(gamma) * calc(epsilon))

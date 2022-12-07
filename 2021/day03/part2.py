def calc(lst):
    res = 0
    for idx in range(len(lst)):
        res += lst[idx] * 2**(len(lst) - (idx + 1))
    return res


file = open("input.txt")

nums = []
for line in file:
    nums.append([int(x) for x in list(line.strip())])

save_nums = [_ for _ in nums]

idx = 0
while len(nums) != 1:
    count = sum([num[idx] for num in nums])
    most_common = 1 if count >= len(nums) / 2 else 0
    nums = [num for num in nums if num[idx] == most_common]
    idx += 1

oxygen_rating = calc(nums[0])

nums = [_ for _ in save_nums]
idx = 0
while len(nums) != 1:
    count = sum([num[idx] for num in nums])
    most_common = 0 if count >= len(nums) / 2 else 1
    nums = [num for num in nums if num[idx] == most_common]
    idx += 1

co2_rating = calc(nums[0])

print(oxygen_rating * co2_rating)

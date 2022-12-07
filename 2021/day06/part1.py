file = open("input.txt")

nums = [int(x) for x in file.readline().split(",")]

for day in range(80):
    idx, max_idx = 0, len(nums)
    while idx < max_idx:
        if nums[idx] == 0:
            nums.append(8)
            nums[idx] = 7
        nums[idx] -= 1
        idx += 1

print(len(nums))

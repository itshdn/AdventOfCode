from collections import Counter

file = open("input.txt")
nums = [int(x) for x in file.read().strip().split(",")]
c = Counter(nums)
cost = [0] * max(nums)

cost[0] = sum(nums)
to_right = len(nums)
to_left = 0

for idx in range(1, len(cost)):
    to_left += c[idx - 1]
    to_right -= c[idx - 1]
    cost[idx] = cost[idx - 1] + to_left - to_right

spot = cost.index(min(cost))

print(sum([abs(num - spot) for num in nums]))

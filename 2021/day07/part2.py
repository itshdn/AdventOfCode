from collections import Counter, defaultdict


def fuel_used(here, there):
    n = abs(here - there)
    return n * (n + 1) // 2


file = open("input.txt")
nums = [int(x) for x in file.read().strip().split(",")]
max_num = max(nums)
cost = defaultdict(int)
c = Counter(nums)

for num in c:
    for idx in range(max_num + 1):
        cost[idx] += c[num] * fuel_used(num, idx)

spot = min(cost, key=cost.get)
print(cost[spot])

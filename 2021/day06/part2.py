from collections import defaultdict, Counter

file = open("input.txt")

nums = [int(x) for x in file.read().strip().split(",")]
c = Counter(nums)
num_fish = defaultdict(int)

for num in c:
    num_fish[num] = c[num]

for day in range(256):
    at0 = num_fish[0]
    for idx in range(8):
        num_fish[idx] = num_fish[idx + 1]
    num_fish[6] += at0
    num_fish[8] = at0

print(sum(num_fish.values()))

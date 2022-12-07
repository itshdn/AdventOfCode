from heapq import heappop, heappush

file = open("input.txt")

elves = []
current_elf = []
for line in file:
    if line == "\n":
        heappush(elves, sum(current_elf))
        current_elf = []
    else:
        current_elf.append(-int(line.strip()))
heappush(elves, sum(current_elf))

top_three_elves = []
for _ in range(3):
    top_three_elves.append(-heappop(elves))

print(f"part1: {top_three_elves[0]}")
print(f"part2: {sum(top_three_elves)}")

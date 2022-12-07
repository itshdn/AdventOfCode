file = open("input.txt")

ans = 0

for line in file:
    elf1, elf2 = line.strip().split(",")
    elf1_start, elf1_end = [int(num) for num in elf1.split("-")]
    elf2_start, elf2_end = [int(num) for num in elf2.split("-")]
    s1 = set([_ for _ in range(elf1_start, elf1_end+1)])
    s2 = set([_ for _ in range(elf2_start, elf2_end + 1)])
    if s1 & s2:
        ans += 1

print(ans)

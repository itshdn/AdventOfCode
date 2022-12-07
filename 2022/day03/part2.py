def calc_priority(letter):
    base = ord("A")-27 if letter.isupper() else ord("a")-1
    return ord(letter) - base


file = open("input.txt")
lines = []
ans = 0

for line in file:
    lines.append(line.strip())

for line_idx in range(0, len(lines), 3):
    group = lines[line_idx:line_idx+3]
    ans += calc_priority((set(group[0]) & set(group[1]) & set(group[2])).pop())

print(ans)

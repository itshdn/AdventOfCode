def calc_priority(letter):
    base = ord("A")-27 if letter.isupper() else ord("a")-1
    return ord(letter) - base


file = open("input.txt")
ans = 0

for line in file:
    pack1 = line.strip()[:len(line)//2]
    pack2 = line[len(line)//2:]
    ans += calc_priority((set(pack1) & set(pack2)).pop())

print(ans)

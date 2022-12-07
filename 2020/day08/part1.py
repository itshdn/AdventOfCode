file = open("input.txt")
ins = []

for line in file:
    words = line.strip().split()
    ins.append([words[0], int(words[1])])

eip = 0
acc = 0
seen = set()

while eip not in seen and eip < len(ins):
    seen.add(eip)
    if ins[eip][0] == "acc":
        acc += ins[eip][1]
    if ins[eip][0] == "jmp":
        eip += ins[eip][1]
        continue
    eip += 1

print(acc)

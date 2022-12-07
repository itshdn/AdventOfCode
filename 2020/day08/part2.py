def change(eip):
    global ins
    if ins[eip][0] == "jmp":
        ins[eip][0] = "nop"
    else:
        ins[eip][0] = "jmp"


def run(change_eip):
    global ins, eip, acc
    seen = set()
    suspects = []
    while eip not in seen and eip < len(ins):
        seen.add(eip)
        if eip == change_eip:
            change(eip)
        if ins[eip][0] == "acc":
            acc += ins[eip][1]
        else:
            suspects.append(eip)
        if ins[eip][0] == "jmp":
            eip += ins[eip][1]
            continue
        eip += 1
    return suspects


def reset():
    global eip, acc
    eip, acc = 0, 0


file = open("input.txt")
ins = []
eip = 0
acc = 0

for line in file:
    words = line.strip().split()
    ins.append([words[0], int(words[1])])

suspects = run(-1)
reset()

for suspect_eip in suspects:
    run(suspect_eip)
    if eip == len(ins):
        print(acc)
        break
    change(suspect_eip)  # change back
    reset()

file = open("input.txt")

starts = ["FCJPHTW", "GRVFZJBH", "HPTR", "ZSNPHT", "NVFZHJCD",
          "PMGFWDZ", "MVZWSJDP", "NDS", "DZSFM"]
stacks = []

for start in starts:
    stacks.append(list(start))

found = False
for line in file:
    if line == '\n':
        found = True
        continue
    if found:
        words = [word for word in line.strip().split()]
        num_to_move = int(words[1])
        move_from = int(words[3]) - 1
        move_to = int(words[5]) - 1
        for _ in range(num_to_move):
            stacks[move_to].append(stacks[move_from].pop())

for stack in stacks:
    print(stack.pop(), end="")

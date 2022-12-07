hor, depth = 0, 0

file = open("input.txt")
for line in file:
    words = [word for word in line.split()]
    value = int(words[1])
    if words[0] == "forward":
        hor += value
    elif words[0] == "down":
        depth += value
    else:
        depth -= value

print(hor * depth)

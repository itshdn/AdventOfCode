hor, aim, depth = 0, 0, 0

file = open("input.txt")
for line in file:
    words = [word for word in line.split()]
    value = int(words[1])
    if words[0] == "forward":
        hor += value
        depth += value * aim
    elif words[0] == "down":
        aim += value
    else:
        aim -= value

print(hor * depth)

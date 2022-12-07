file = open("input.txt")

line = file.readline().strip()

for idx in range(3, len(line)-1):
    s = set(line[idx-3:idx+1])
    if len(s) == 4:
        print(idx+1)
        break

for idx in range(13, len(line)-1):
    s = set(line[idx-13:idx+1])
    if len(s) == 14:
        print(idx+1)
        break

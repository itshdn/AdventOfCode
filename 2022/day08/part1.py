file = open("input.txt")

grid = []
count = 0

for line in file:
    grid.append([int(n) for n in list(line.strip())])

for row in range(1, len(grid[0]) - 1):
    for col in range(1, len(grid) - 1):
        this_num = grid[row][col]
        side = []
        for this_row in range(row-1, -1, -1):
            side.append(grid[this_row][col])
        if this_num > max(side):
            count += 1
            continue
        side = []
        for this_row in range(row+1, len(grid)):
            side.append(grid[this_row][col])
        if this_num > max(side):
            count += 1
            continue
        side = []
        for this_col in range(col-1, -1, -1):
            side.append(grid[row][this_col])
        if this_num > max(side):
            count += 1
            continue
        side = []
        for this_col in range(col+1, len(grid[0])):
            side.append(grid[row][this_col])
        if this_num > max(side):
            count += 1
            continue
        side = []

print(count + (len(grid[0])*2) + (len(grid)-2)*2)

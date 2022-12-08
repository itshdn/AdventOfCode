file = open("input.txt")

grid = []
scores = []

for line in file:
    grid.append([int(n) for n in list(line.strip())])

for row in range(1, len(grid[0]) - 1):
    for col in range(1, len(grid) - 1):
        this_num = grid[row][col]
        side = []
        score = 1
        for this_row in range(row-1, -1, -1):
            side.append(grid[this_row][col])
        this_score = 0
        for num in side:
            this_score += 1
            if num >= this_num:
                break
        score *= this_score

        side = []
        for this_row in range(row+1, len(grid)):
            side.append(grid[this_row][col])
        this_score = 0
        for num in side:
            this_score += 1
            if num >= this_num:
                break
        score *= this_score

        side = []
        for this_col in range(col-1, -1, -1):
            side.append(grid[row][this_col])
        this_score = 0
        for num in side:
            this_score += 1
            if num >= this_num:
                break
        score *= this_score

        side = []
        for this_col in range(col+1, len(grid[0])):
            side.append(grid[row][this_col])
        this_score = 0
        for num in side:
            this_score += 1
            if num >= this_num:
                break
        score *= this_score

        scores.append(score)


print(max(scores))

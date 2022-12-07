from lib import *

file = open("input.txt")

grid = []
for line in file:
    grid.append([Octopus(int(n)) for n in list(line.strip())])

for row in range(len(grid)):
    for col in range(len(grid[0])):
        grid[row][col].set_adjacent_octopuses(grid, row, col)

this_step = 1
while True:
    step(grid)
    if all_flashed(grid):
        print(this_step)
        break
    this_step += 1

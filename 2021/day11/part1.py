from lib import *

file = open("input.txt")

grid = []
for line in file:
    grid.append([Octopus(int(n)) for n in list(line.strip())])

for row in range(len(grid)):
    for col in range(len(grid[0])):
        grid[row][col].set_adjacent_octopuses(grid, row, col)

for this_step in range(100):
    step(grid)

print(Octopus.total_flashes)

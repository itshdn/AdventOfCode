from lib import *

file = open("input.txt")
past = False
points = []
folds = []

for line in file:
    if line == "\n":
        past = True
        continue
    if not past:
        a, b = [int(x) for x in line.strip().split(",")]
        points.append((a, b))
    else:
        word = [_ for _ in line.strip().split()][-1]
        a, b = [x for x in word.split("=")]
        folds.append((a, int(b)))

max_coord = max(max([point[0] for point in points]), max([point[1] for point in points]))
grid = Grid(max_coord, points)

for fold in folds:
    grid.fold(fold[0], fold[1])

grid.print()

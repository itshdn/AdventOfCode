from lib import *
import functools
import operator

file = open("input.txt")

graph = []
for line in file:
    graph.append([Node(int(x)) for x in list(line.strip())])

for row in range(len(graph)):
    for col in range(len(graph[0])):
        graph[row][col].set_next(graph, row, col)

low_points = []
for row in graph:
    for node in row:
        if node.is_low_point():
            low_points.append(node)

basin_sizes = []
for low_point in low_points:
    visited = set()
    visited.add(low_point)
    basin_sizes.append(basin_size(low_point, visited))

print(functools.reduce(operator.mul, sorted(basin_sizes)[-3:]))

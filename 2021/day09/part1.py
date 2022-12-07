from lib import *

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

print(sum([node.value + 1 for node in low_points]))

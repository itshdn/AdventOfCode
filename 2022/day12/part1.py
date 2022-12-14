from lib import *
from heapq import heappush, heappop

file = open("input.txt")

grid = []

for line in file:
    grid.append(list(line.strip()))

for row_idx in range(len(grid)):
    for col_idx in range(len(grid[0])):
        if grid[row_idx][col_idx] == "S":
            S = grid[row_idx][col_idx] = Node(1, row_idx, col_idx)
        elif grid[row_idx][col_idx] == "E":
            E = grid[row_idx][col_idx] = Node(26, row_idx, col_idx)
        else:
            value = ord(grid[row_idx][col_idx]) - (ord("a") - 1)
            grid[row_idx][col_idx] = Node(value, row_idx, col_idx)

for row_idx in range(len(grid)):
    for col_idx in range(len(grid[0])):
        grid[row_idx][col_idx].set_edges(grid, row_idx, col_idx)

visited = set()
queue = [[S.distance, S.euc_dis(E), (S.row, S.col)]]

while True:
    this_row, this_col = heappop(queue)[2]
    this_node: Node = grid[this_row][this_col]

    if this_node == E:
        print(E.distance)
        break
    if this_node in visited:
        continue
    visited.add(this_node)

    valid_edges = this_node.get_valid_edges_part1(visited)

    for node in valid_edges:
        node.distance = this_node.distance + 1
        heappush(queue, [node.distance, node.euc_dis(E), (node.row, node.col)])

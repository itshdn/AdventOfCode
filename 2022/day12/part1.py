from lib import *
from heapq import heappush, heappop
from math import sqrt


def djik(queue, visited):
    global grid, E
    this_row, this_col = heappop(queue)[2]
    this_node = grid[this_row][this_col]

    if E in visited:
        print(E.distance)
        return

    valid_edges = this_node.get_valid_edges(visited)

    for node in valid_edges:
        euc = euc_dis((node.row, node.col), (E.row, E.col))
        if node.distance == 0:
            node.distance = this_node.distance + 1
        else:
            node.distance = min(node.distance, this_node.distance + 1)
        heappush(queue, [node.distance, euc, (node.row, node.col)])
        visited.add(node)

    djik(queue, visited)


def euc_dis(start, end):
    x = abs(start[0] - end[0])
    y = abs(start[1] - end[1])
    return sqrt(x**2 + y**2)


file = open("input.txt")

grid = []
S, E = 0, 0

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
queue = [[0, euc_dis((S.row, S.col), (E.row, E.col)), (E.row, E.col)]]

while True:
    this_row, this_col = heappop(queue)[2]
    this_node = grid[this_row][this_col]

    if this_node.value == 1:
        print(this_node.distance)
        break
    if this_node in visited:
        continue
    visited.add(this_node)

    valid_edges = this_node.get_valid_edges(visited)

    for node in valid_edges:
        euc = euc_dis((node.row, node.col), (S.row, S.col))
        node.distance = this_node.distance + 1
        heappush(queue, [node.distance, euc, (node.row, node.col)])
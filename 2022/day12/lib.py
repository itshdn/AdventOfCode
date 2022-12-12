from math import sqrt


class Node:
    def __init__(self, val, row, col):
        self.value = val
        self.edges = []
        self.distance = 0
        self.row = row
        self.col = col

    def set_edges(self, grid, row, col):
        if row > 0:
            self.edges.append(grid[row-1][col])
        if row < (len(grid) - 1):
            self.edges.append(grid[row+1][col])
        if col > 0:
            self.edges.append(grid[row][col-1])
        if col < (len(grid[0]) - 1):
            self.edges.append(grid[row][col+1])

    def get_valid_edges_part1(self, visited):
        res = []
        for node in self.edges:
            if node not in visited and node.value - self.value <= 1:
                res.append(node)
        return res

    def get_valid_edges_part2(self, visited):
        res = []
        for node in self.edges:
            if node not in visited and node.value - self.value >= -1:
                res.append(node)
        return res

    def euc_dis(self, end):
        x = abs(self.row - end.row)
        y = abs(self.col - end.col)
        return sqrt(x**2 + y**2)

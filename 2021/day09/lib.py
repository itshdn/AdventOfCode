class Node:
    def __init__(self, value):
        self.value = value
        self.next = [None] * 4

    def set_next(self, graph, row, col):
        self.next[0] = graph[row-1][col] if row != 0 else None
        self.next[1] = graph[row+1][col] if row != len(graph) - 1 else None
        self.next[2] = graph[row][col-1] if col != 0 else None
        self.next[3] = graph[row][col+1] if col != len(graph[0]) - 1 else None

    def is_low_point(self):
        neighbors = [node for node in self.next if node]
        return all([self.value < node.value for node in neighbors])


def basin_size(this_node, visited):
    size_below = 0
    neighbors = []

    for next_node in this_node.next:
        if next_node and (next_node not in visited) and (next_node.value != 9):
            neighbors.append(next_node)
            visited.add(next_node)

    for next_node in neighbors:
        size_below += basin_size(next_node, visited)

    return 1 + size_below

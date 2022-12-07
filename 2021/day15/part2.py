from heapq import heapify, heappop, heappush


def add(n, m):
    res = n + m
    if res > 9:
        res -= 9
    return res


file = open("input.txt")

nums = []
nums_big = []
muls = [list(range(5))]

for row in range(1, 5):
    muls.append([x+1 for x in muls[row-1]])

for line in file:
    nums.append([int(x) for x in list(line.strip())])

nums_rows = len(nums)
nums_cols = len(nums[0])
for row in range(nums_rows * 5):
    nums_big.append([0] * nums_cols * 5)

for row_mul in range(5):
    for col_mul in range(5):
        row_offset = nums_rows * row_mul
        col_offset = nums_cols * col_mul
        for row in range(len(nums)):
            for col in range(len(nums[0])):
                nums_big[row + row_offset][col + col_offset] = add(nums[row][col], muls[row_mul][col_mul])

rows, cols = len(nums_big), len(nums_big[0])
dist_to = {(0, 0): 0}
distances = []
heappush(distances, (0, (0, 0)))
visited = set()

while (rows-1, cols-1) not in dist_to:
    cur = heappop(distances)[1]
    visited.add(cur)
    row, col = cur[0], cur[1]
    if row != len(nums_big) - 1 and (row + 1, col) not in visited:
        dist_to[(row+1, col)] = dist_to[(row, col)] + nums_big[row+1][col]
        heappush(distances, (dist_to[(row+1, col)], (row+1, col)))
        visited.add((row+1, col))
    if col != len(nums_big[0])-1 and (row, col+1) not in visited:
        dist_to[(row, col+1)] = dist_to[(row, col)] + nums_big[row][col+1]
        heappush(distances, (dist_to[(row, col+1)], (row, col+1)))
        visited.add((row, col+1))
    if row != 0 and (row-1, col) not in visited:
        dist_to[(row-1, col)] = dist_to[(row, col)] + nums_big[row-1][col]
        heappush(distances, (dist_to[(row-1, col)], (row-1, col)))
        visited.add((row-1, col))
    if col != 0 and (row, col-1) not in visited:
        dist_to[(row, col-1)] = dist_to[(row, col)] + nums_big[row][col-1]
        heappush(distances, (dist_to[(row, col-1)], (row, col-1)))
        visited.add((row, col-1))

print(dist_to[rows-1, cols-1])

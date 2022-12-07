def calc_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def calc_b(x1, y1, m):
    return -m*x1 + y1


grid = [[0 for _ in range(1001)] for _ in range(1000)]
file = open("input.txt")

for line in file:
    points = line.strip().split(" -> ")
    points = [point.split(",") for point in points]

    x1 = int(points[0][0])
    y1 = int(points[0][1])
    x2 = int(points[1][0])
    y2 = int(points[1][1])

    if x1 != x2:
        m = calc_slope(x1, y1, x2, y2)
        b = calc_b(x1, y1, m)
        x1, x2 = min([x1, x2]), max([x1, x2])
        for x in range(x1, x2 + 1):
            y = m*x + b
            if y == int(y):
                grid[int(y)][x] += 1
    else:
        y1, y2, = min([y1, y2]), max([y1, y2])
        for y in range(y1, y2 + 1):
            grid[y][x1] += 1

ans = 0
for row in grid:
    for col in range(len(row)):
        if row[col] > 1:
            ans += 1
print(ans)

class Grid:
    def __init__(self, max_coord, points):
        self.grid = []
        self.fill_grid(max_coord, points)

    def fill_grid(self, max_coord, points):
        for row in range(max_coord+1):
            self.grid.append([])
            for col in range(max_coord+1):
                self.grid[row].append(False)
        for point in points:
            x, y = point[0], point[1]
            self.grid[y][x] = True

    def count(self):
        result = 0
        for row in self.grid:
            for spot in row:
                result += spot
        return result

    def fold(self, xy, fold_coord):
        self.x_fold(fold_coord) if xy == "x" else self.y_fold(fold_coord)

    def x_fold(self, fold_col):
        num_rows, num_cols = len(self.grid), len(self.grid[0])
        for row in range(num_rows):
            for col in range(fold_col+1, num_cols):
                d = col - fold_col
                outside = self.grid[row][col]
                inside = self.grid[row][fold_col-d]
                self.grid[row][fold_col-d] = (outside | inside)
        for row in range(len(self.grid)):
            self.grid[row] = self.grid[row][:fold_col]

    def y_fold(self, fold_row):
        num_rows, num_cols = len(self.grid), len(self.grid[0])
        for row in range(fold_row+1, num_rows):
            for col in range(num_cols):
                d = row - fold_row
                outside = self.grid[row][col]
                inside = self.grid[fold_row-d][col]
                self.grid[fold_row-d][col] = (outside | inside)
        for row in range(len(self.grid)):
            self.grid = self.grid[:fold_row]

    def print(self):
        for row in self.grid:
            new_row = []
            for spot in row:
                if spot:
                    new_row.append("#")
                else:
                    new_row.append('.')
            print(*new_row)

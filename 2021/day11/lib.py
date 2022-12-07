class Octopus:
    total_flashes = 0

    def __init__(self, starting_energy):
        self.energy = starting_energy
        self.adjacent_octopuses = []
        self.flashed = False

    def set_adjacent_octopuses(self, grid, row, col):  # goes clockwise starting from top
        self.adjacent_octopuses.append(grid[row-1][col] if row != 0 else None)
        self.adjacent_octopuses.append(grid[row-1][col+1] if row != 0 and col != len(grid[0]) - 1 else None)
        self.adjacent_octopuses.append(grid[row][col+1] if col != len(grid[0]) - 1 else None)
        self.adjacent_octopuses.append(grid[row+1][col+1] if row != len(grid) - 1 and col != len(grid[0]) - 1 else None)
        self.adjacent_octopuses.append(grid[row+1][col] if row != len(grid) - 1 else None)
        self.adjacent_octopuses.append(grid[row+1][col-1] if row != len(grid) - 1 and col != 0 else None)
        self.adjacent_octopuses.append(grid[row][col-1] if col != 0 else None)
        self.adjacent_octopuses.append(grid[row-1][col-1] if row != 0 and col != 0 else None)

    def check_flash(self):
        if self.energy > 9:
            self.flash()

    def flash(self):
        self.flashed = True
        Octopus.total_flashes += 1
        self.energy = 0

        for adjacent_octopus in self.adjacent_octopuses:
            if adjacent_octopus and (not adjacent_octopus.flashed):
                adjacent_octopus.energy += 1

        for adjacent_octopus in self.adjacent_octopuses:
            if adjacent_octopus:
                adjacent_octopus.check_flash()


def step(grid):
    for row in grid:
        for octopus in row:
            octopus.flashed = False
            octopus.energy += 1
    for row in grid:
        for octopus in row:
            octopus.check_flash()


def all_flashed(grid):
    for row in grid:
        for octopus in row:
            if not octopus.flashed:
                return False
    return True

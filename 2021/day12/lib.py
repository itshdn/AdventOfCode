class CaveNetwork:
    def __init__(self):
        self.start = None
        self.end = None
        self.caves = {}
        self.caves_been_to = set()

    def reset(self):
        self.caves_been_to = set()
        for cave in self.caves:
            self.caves[cave].reset()

    def scan(self, this_cave):
        if this_cave == self.end:
            return

        if not (this_cave.big or this_cave.twice):
            self.caves_been_to.add(this_cave)

        if this_cave.twice:
            this_cave.times_visited += 1
            if this_cave.times_visited == 2:
                self.caves_been_to.add(this_cave)

        valid_next_caves = []
        for next_cave in this_cave.connected_caves:
            if next_cave not in self.caves_been_to:
                valid_next_caves.append(next_cave)

        for next_cave in valid_next_caves:
            next_cave.num_paths += 1

        for next_cave in valid_next_caves:
            self.scan(next_cave)

        if not (this_cave.big or this_cave.twice):
            self.caves_been_to.remove(this_cave)

        if this_cave.twice:
            this_cave.times_visited -= 1
            if this_cave in self.caves_been_to:
                self.caves_been_to.remove(this_cave)


class Cave:
    def __init__(self, is_big):
        self.big = is_big
        self.connected_caves = []
        self.num_paths = 0
        self.times_visited = 0
        self.twice = False

    def add_connecting_cave(self, other_cave):
        self.connected_caves.append(other_cave)

    def reset(self):
        self.num_paths = 0
        self.times_visited = 0
        self.twice = False

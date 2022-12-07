from lib import *

file = open("input.txt")

cave_network = CaveNetwork()

for line in file:  # build cave network
    cave1, cave2 = [cave for cave in line.strip().split("-")]
    if cave1 not in cave_network.caves:
        cave_network.caves[cave1] = Cave(cave1.isupper())
    if cave2 not in cave_network.caves:
        cave_network.caves[cave2] = Cave(cave2.isupper())

    cave_network.caves[cave1].add_connecting_cave(cave_network.caves[cave2])
    cave_network.caves[cave2].add_connecting_cave(cave_network.caves[cave1])

    if cave1 == "start":
        cave_network.start = cave_network.caves[cave1]
    if cave2 == "start":
        cave_network.start = cave_network.caves[cave2]

    if cave1 == "end":
        cave_network.end = cave_network.caves[cave1]
    if cave2 == "end":
        cave_network.end = cave_network.caves[cave2]

cave_network.start.num_paths = 1
cave_network.scan(cave_network.start)
without_visiting_any_twice = cave_network.end.num_paths

num_paths_per_twice_choice = []
for cave in cave_network.caves:
    cave = cave_network.caves[cave]
    start = cave == cave_network.start
    end = cave == cave_network.end
    if not (cave.big or start or end):
        cave_network.reset()
        cave_network.start.num_paths = 1
        cave.twice = True
        cave_network.scan(cave_network.start)
        num_paths_per_twice_choice.append(cave_network.end.num_paths - without_visiting_any_twice)

print(sum(num_paths_per_twice_choice) + without_visiting_any_twice)

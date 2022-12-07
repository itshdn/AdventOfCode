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
print(cave_network.end.num_paths)

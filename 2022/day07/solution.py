from lib import *


def dfs(cur_dir):
    global sizes, ans
    sizes[cur_dir] = sum(cur_dir.files)
    for child in cur_dir.directories.values():
        dfs(child)
        sizes[cur_dir] += sizes[child]
    ans += sizes[cur_dir] if sizes[cur_dir] <= 100000 else 0


file = open("input.txt")
fs = FileSystem(Directory("/", None))
sizes = {}
ans = 0

for line in file:
    words = line.strip().split()
    if words[0] == "$":
        if words[1] == "cd":
            fs.cd(words[2])
    elif words[0] == "dir":
        fs.pwd.add_directory(words[1])
    else:
        fs.pwd.add_file(int(words[0]))

dfs(fs.root)
print(f"part1: {ans}")

free_space = 70000000 - sizes[fs.root]
need_to_delete = 30000000 - free_space
possible = []
for size in sizes.values():
    if size >= need_to_delete:
        possible.append(size)

print(f"part2: {sorted(possible)[0]}")

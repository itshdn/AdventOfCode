from collections import defaultdict
import math


def solve(step, depth, pair_counts, rules):
    if step == depth:
        return pair_counts

    new_pair_counts = defaultdict(int)

    for pair in pair_counts:
        new_pair_counts[pair[0]+rules[pair]] += pair_counts[pair]
        new_pair_counts[rules[pair]+pair[1]] += pair_counts[pair]

    return solve(step + 1, depth, new_pair_counts, rules)


file = open("input.txt")

rules = {}
template = []
pair_counts = defaultdict(int)
letter_counts = defaultdict(int)

past = False
for line in file:
    if line == "\n":
        past = True
        continue
    if not past:
        template = list(line.strip())
    else:
        words = [word for word in line.strip().split(" -> ")]
        rules[words[0]] = words[1]

for idx in range(len(template)-1):
    pair_counts[template[idx]+template[idx+1]] += 1

pair_counts = solve(0, 40, pair_counts, rules)

for pair in pair_counts:
    for letter in pair:
        letter_counts[letter] += pair_counts[pair]

max_idx = max(letter_counts, key=letter_counts.get)
min_idx = min(letter_counts, key=letter_counts.get)

most = math.ceil(letter_counts[max_idx] / 2)
least = math.ceil(letter_counts[min_idx] / 2)
print(most - least)

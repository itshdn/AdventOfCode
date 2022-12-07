file = open("input.txt")

scores_for_hand = {"X": 1, "Y": 2, "Z": 3}
win = {"X": "C", "Y": "A", "Z": "B"}
loss = {"X": "B", "Y": "C", "Z": "A"}
draw = {"X": "A", "Y": "B", "Z": "C"}
score = 0

for line in file:
    them, me = [letter for letter in line.strip().split()]
    if me == "X":
        score += scores_for_hand[me]
        if them == win[me]: score += 6
        if them == draw[me]: score += 3
    if me == "Y":
        score += scores_for_hand[me]
        if them == win[me]: score += 6
        if them == draw[me]: score += 3
    if me == "Z":
        score += scores_for_hand[me]
        if them == win[me]: score += 6
        if them == draw[me]: score += 3

print(score)

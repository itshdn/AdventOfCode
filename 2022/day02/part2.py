file = open("input.txt")

scores_for_hand = {"X": 1, "Y": 2, "Z": 3}
win = {"A": "Y", "B": "Z", "C": "X"}
loss = {"A": "Z", "B": "X", "C": "Y"}
draw = {"A": "X", "B": "Y", "C": "Z"}
score = 0

for line in file:
    them, need_to_do = [letter for letter in line.strip().split()]
    if need_to_do == "X":  # lose
        score += scores_for_hand[loss[them]]
    elif need_to_do == "Y":  # draw
        score += 3 + scores_for_hand[draw[them]]
    else:  # win
        score += 6 + scores_for_hand[win[them]]

print(score)

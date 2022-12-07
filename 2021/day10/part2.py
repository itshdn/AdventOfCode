scores = {")": 1, "]": 2, "}": 3, ">": 4}
close_to_open = {")": "(", "]": "[", "}": "{", ">": "<"}
open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
openings = {"(", "[", "{", "<"}
closings = {")", "]", "}", ">"}

file = open("input.txt")

lines = []
for line in file:
    lines.append(line.strip())

completion_string_scores = []

for line in lines:
    stack = []
    corrupted = False

    for char in line:
        if char in openings:
            stack.append(char)
        else:  # char in closings
            if len(stack) == 0 or stack[-1] != close_to_open[char]:
                corrupted = True
                break  # corrupted, discard
            stack.pop()  # closing matches opening on top of stack

    if (not corrupted) and len(stack) > 0:  # is incomplete
        completion_string = []
        while len(stack) > 0:  # fill completion string with remaining openings
            completion_string.append(open_to_close[stack.pop()])

        score = 0  # calc score
        for closing in completion_string:
            score *= 5
            score += scores[closing]

        completion_string_scores.append(score)  # record this line's score

completion_string_scores.sort()
print(completion_string_scores[len(completion_string_scores) // 2])

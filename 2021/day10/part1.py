scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
match = {")": "(", "]": "[", "}": "{", ">": "<"}
openings = {"(", "[", "{", "<"}
closings = {")", "]", "}", ">"}

file = open("input.txt")

lines = []
for line in file:
    lines.append(line.strip())


score = 0

for line in lines:
    stack = []
    for char in line:
        if char in openings:
            stack.append(char)
        else:  # char in closings
            if len(stack) == 0 or stack[-1] != match[char]:
                score += scores[char]
                break
            stack.pop()

print(score)

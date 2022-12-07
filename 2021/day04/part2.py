def mark_boards(boards, num):
    for board in boards:
        for row in board:
            for col in range(len(row)):
                if row[col] == num:
                    row[col] = 'X'


def check_boards(boards):
    winning_boards = []
    for board in boards:
        for row in board:
            row = [val == 'X' for val in row]
            if all(row):
                winning_boards.append(board)
        for col in range(len(board[0])):
            col = [row[col] == 'X' for row in board]
            if all(col):
                winning_boards.append(board)
    return winning_boards


def calc_score(board):
    res = 0
    for row in board:
        for col in range(len(row)):
            res += row[col] if row[col] != 'X' else 0
    return res


file = open("input.txt")

nums = [int(x) for x in file.readline().split(",")]
boards = []

board_lines = []

while file.readline():
    board = []
    for _ in range(5):
        board.append([int(x) for x in file.readline().split()])
    boards.append(board)

num_idx = 0
while len(boards) > 1:
    mark_boards(boards, nums[num_idx])
    winning_boards = check_boards(boards)
    if len(winning_boards) > 0:
        boards = [board for board in boards if board not in winning_boards]
    num_idx += 1

winning_boards = []
while len(winning_boards) == 0:
    mark_boards(boards, nums[num_idx])
    winning_boards = check_boards(boards)
    num_idx += 1

print(nums[num_idx - 1] * calc_score(winning_boards[0]))

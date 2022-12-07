def mark_boards(boards, num):
    for board in boards:
        for row in board:
            for col in range(len(row)):
                if row[col] == num:
                    row[col] = 'X'


def check_boards(boards):
    for board in boards:
        for row in board:
            row = [val == 'X' for val in row]
            if all(row):
                return board
        for col in range(len(board[0])):
            col = [row[col] == 'X' for row in board]
            if all(col):
                return board


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

for num in nums:
    mark_boards(boards, num)
    board = check_boards(boards)
    if board:
        print(num * calc_score(board))
        break

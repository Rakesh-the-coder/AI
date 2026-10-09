def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:

        if board[i][j] == 'Q':
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < 8:

        if board[i][j] == 'Q':
            return False

        i -= 1
        j += 1

    return True


def solve_8_queens(board, row):

    if row == 8:
        return True

    for col in range(8):

        if is_safe(board, row, col):

            board[row][col] = 'Q'

            if solve_8_queens(board, row + 1):
                return True

            board[row][col] = '.'

    return False


board = [
    ['.' for _ in range(8)]
    for _ in range(8)
]

if solve_8_queens(board, 0):

    print("===== 8 QUEENS SOLUTION =====")

    for row in board:
        print(" ".join(row))

else:
    print("No solution exists.")
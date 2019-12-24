

def isSafe(board, row, col, N):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col, n):

    if col >= n:
        return True

    for i in range(n):

        if isSafe(board, i , col, n):
            board[i][col] = 1

            if solve(board, col + 1, n):
                return True

            board[i][col] = 0

    return False





board = [ [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0] ]


solve(board, 0, 4)


for i in range(4):
    for j in range(4):
        print board[i][j]



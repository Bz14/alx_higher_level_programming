import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N, result):
    if col >= N:
        result.append(board.copy())
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, result) or res
            board[i][col] = 0

    return res


def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        return 1

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        return 1

    board = [[0] * N for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)

    for sol in result:
        for row in sol:
            print(' '.join(map(str, row)))
        print()

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    sys.exit(solve_n_queens(sys.argv[1]))

#!/usr/bin/python3
"""
The N-Queens problem.
"""
import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """Backtracking to find all solutions."""
    if row == n:
        print([[r, c] for r in range(n) for c in range(n) if board[r][c]])
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solve the N-Queens problem.
    Args:
        n (int): Number of queens, must be >= 4.
    """
    cols, pos_diag, neg_diag = set(), set(), set()
    board = [[0] * n for _ in range(n)]
    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

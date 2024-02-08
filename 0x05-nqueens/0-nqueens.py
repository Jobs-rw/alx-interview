#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(n, board):
    """
    Backtrack function to find solutions
    """
    r = 0
    cols = set()
    pos_diag = set()
    neg_diag = set()

    while r < n:
        c = 0
        while c < n:
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                c += 1
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 1

            if r == n - 1:
                res = []
                for l in range(len(board)):
                    for k in range(len(board[l])):
                        if board[l][k] == 1:
                            res.append([l, k])
                print(res)
                
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = 0
                c += 1
            else:
                r += 1
                break

        if c == n:
            if r == 0:
                break
            else:
                r -= 1
                last_queen_col = board[r].index(1)
                cols.remove(last_queen_col)
                pos_diag.remove(r + last_queen_col)
                neg_diag.remove(r - last_queen_col)
                board[r][last_queen_col] = 0
                c = last_queen_col + 1


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    board = [[0] * n for _ in range(n)]
    backtrack(n, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

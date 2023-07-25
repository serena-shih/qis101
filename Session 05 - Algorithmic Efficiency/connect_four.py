#!/usr/bin/env python3
"""connect_four.py"""

def check_straight(ls : list[int]):
    for i in range(len(ls) - 4):
        if (ls[i], ls[i+1], ls[i+2], ls[i+3]) == (1,1,1,1):
            return 1
        if (ls[i], ls[i+1], ls[i+2], ls[i+3]) == (2,2,2,2):
            return 2
    return 0

def check_diag(b : list[list[int]]):
    for r in range(len(b) - 3):
        for c in range(len(b[0]) - 3):
            if (b[r][c], b[r+1][c+1], b[r+2][c+2], b[r+3][c+3]) == (1,1,1,1):
                return 1
            if (b[r][c], b[r+1][c+1], b[r+2][c+2], b[r+3][c+3]) == (2,2,2,2):
                return 2
        for c in range(3, len(b[0])):
            if (b[r][c], b[r+1][c-1], b[r+2][c-2], b[r+3][c-3]) == (1,1,1,1):
                return 1
            if (b[r][c], b[r+1][c-1], b[r+2][c-2], b[r+3][c-3]) == (2,2,2,2):
                return 2
    return 0

def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")
    for row in board:
        if check_straight(row) != 0:
            print(f"The winner is {check_straight(row)}\n")
            return
    for col in list(zip(*board)):
        if check_straight(col) != 0:
            print(f"The winner is {check_straight(col)}\n")
            return
    if check_diag(board) != 0:
        print(f"The winner is {check_diag(board)}\n")
        return
    print("There is no winner")
    print()


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()

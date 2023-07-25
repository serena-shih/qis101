#!/usr/bin/env python3
"""board_encoding.py"""

from numpy import base_repr

def print_board(board : int) -> str:
    """Outputs string representation of tic-tac-toe board"""
    board_str : str = base_repr(board, 3)
    rev : str = "".join(reversed(board_str))
    for _ in range(9 - len(rev)):
        rev += "0"
    
    printed_str : str = f"[{rev[0]}, {rev[1]}, {rev[2]}]\n"
    printed_str += f"[{rev[3]}, {rev[4]}, {rev[5]}]\n"
    printed_str += f"[{rev[6]}, {rev[7]}, {rev[8]}]\n"

    return printed_str

def main():
    board1 : str = print_board(2271)
    board2 : str = print_board(1638)
    board3 : str = print_board(12065)

    print(f"Board corresponding to 2271:\n{board1}")
    print(f"Board corresponding to 1638:\n{board2}")
    print(f"Board corresponding to 12065:\n{board3}")

if __name__ == "__main__":
    main()
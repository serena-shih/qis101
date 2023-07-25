#!/usr/bin/env python3
"""sum_multiples.py"""

def main() -> None:
    sum_mult : int = 0
    for i in range(1900):
        if (i % 7 == 0) and (i % 11 == 0):
            sum_mult += i
    print(f"Sum: {sum_mult:,}")

if __name__ == "__main__":
    main()
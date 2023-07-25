#!/usr/bin/env python3
"""sum_squares.py"""

def sum_sq(n : int) -> int:
    """Calculates the sum of squares up to and including n"""
    s : int = 0
    for i in range(n+1):
        s += i**2
    return s

def gauss_sum(n : int) -> float:
    """Calculates sum of squares using Gauss's formula"""
    return (2 * n**3 + 3 * n**2 + n) / 6

def main() -> None:
    print(f"Loop sum: {sum_sq(1000):,}")
    print(f"Gaussian summation: {gauss_sum(1000):,}")

if __name__ == "__main__":
    main()
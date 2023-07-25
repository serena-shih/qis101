#!/usr/bin/env python3
"""herons_method.py"""

from random import randint

def find_sqrt(s : int):
    """Approximate the square root of s within 10**(-8) of actual value"""
    x : float = s / 2
    while abs(s - (x * x)) > (10**(-8)):
        x = 0.5 * (s + x*x) / x
    return x

def main():
    s : int = randint(10**6, 2*(10**6))
    r : float = find_sqrt(s)
    print(f"s = {s}, r = {r:.8f}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd

def calc_lcm(a : int, b : int):
    """Calculates lowest common multiple of a and b"""
    if a > b:
        a, b = b, a
    divisor : int = gcd(a, b)
    div_b : int = b // divisor
    return div_b * a

def main():
    a : int = 447618
    b : int = 2011835
    lcm = calc_lcm(a, b)
    print(f"LCM of {a} and {b} = {lcm}")

if __name__ == "__main__":
    main()
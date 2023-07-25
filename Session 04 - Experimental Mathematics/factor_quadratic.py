#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd

def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Hx^2 + Ix + J"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")

    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    if a * d + b * c == i:
                        gcd1 : int = gcd(a, b)
                        gcd2 : int = gcd(c, d)
                        gcd_factor : int = gcd1 * gcd2
                        print(f"GCD of H, I, J = {gcd_factor}")
                        print(f"The factors are: {gcd_factor}" + 
                              f"({a // gcd1}x + {b // gcd1})" + 
                              f"({c // gcd2}x + {d // gcd2})")
                        return


def main() -> None:
    factor_quadratic(115425, 3254121, 379020)


if __name__ == "__main__":
    main()

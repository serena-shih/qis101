#!/usr/bin/env python3
"""gen_continued_fractions.py"""

import math

MAX_TERMS: int = 20


def decode_gencf(form: tuple[int, ...]) -> float:
    """Evaluates a generalized continued fraction of the given form"""
    a0, b0, Ai, Bi, Ci, Di, Ei = form
    an, bn = a0, b0
    hn, kn = 0.0, 0.0
    b_1, h_1, k_1 = 1.0, 1.0, 0.0
    h_2, k_2 = 0.0, 1.0
    for n in range(1, MAX_TERMS):
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
        an = Di * n + Ei
        bn = Ai * n * n + Bi * n + Ci
    return hn / kn


def print_rel_error(estimated: float, actual: float) -> None:
    print(f"Est.        : {estimated}")
    print(f"Act.        : {actual}")
    print(f"Rel. % Err  : {(actual - estimated)/actual:.14%}\n")


def main() -> None:
    print("Euler's Generalized Continued Fraction for Pi")
    x: float = decode_gencf((3, 1, 4, 4, 1, 0, 6))
    print_rel_error(x, math.pi)

    print("\nProfessor Biersach's GCF #1 for pi")
    y: float = decode_gencf((3, 1, 8, 0, -7, 8, -1))
    print_rel_error(y, math.pi)

    print("\nProfessor Biersach's GCF #2 for pi")
    z: float = decode_gencf((2, 8, 4, 8, 0, 4, 2))
    print_rel_error(z, math.pi)


if __name__ == "__main__":
    main()

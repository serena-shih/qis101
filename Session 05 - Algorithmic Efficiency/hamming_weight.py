#!/usr/bin/env python3
"""hamming_weight.py"""

def hamming(pop : int):
    """Calculates number of 1's in binary representation of pop"""

    bin_len : int = len(bin(pop))
    count : int = 0
    for _ in range(bin_len):
        if pop % 2 == 1:
            count = count + 1
        pop = pop >> 1
    return count


def main():
    population : int = 95601
    print(f"My hamming weight of {population} = {hamming(population)}")
    print(f"Python's hamming weight of {population} = {bin(population).count('1')}")

if __name__ == "__main__":
    main()
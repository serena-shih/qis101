#!/usr/bin/env python3
"""prime_racer4.py"""

from math import sqrt
from random import seed, randint
from time import process_time

def gen_primes():
    """Generates list of all primes less than 1000"""
    primes : list[int] = []
    for i in range(2, 1000):
        if i % 2 != 0 and all(i % factor != 0 for factor in range(3, int(sqrt(i)), 2)):
            primes.append(i)
    return primes

def is_prime(n : int, primes):
    """Checks if n is prime"""
    if n % 2 == 0:
        return False
    return all(n % factor != 0 for factor in primes)

def main() -> None:
    seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    primes : list[int] = gen_primes()

    start_time: float = process_time()
    num_primes: int = [is_prime(n, primes) for n in samples].count(True)
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")

if __name__ == "__main__":
    main()
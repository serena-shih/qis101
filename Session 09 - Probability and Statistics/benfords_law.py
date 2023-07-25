#!/usr/bin/env python3
"""benfords_law.py"""

from __future__ import annotations
import typing
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    np.random.seed(2023)

    digits: list[int] = list(range(1, 10))

    n: int = 100000
    nums: list[int] = [(rand.randint(1, 1000001)) ** 100 for _ in range(n + 1)]

    msds: list[int] = [0 for _ in range(9)]
    for i in nums:
        s: str = str(i)
        msd: int = int(s[0])
        msds[msd-1] = msds[msd-1] + 1
    msd_prob: NDArray[np.float_] = np.asarray(
        [(msds[i] / (n + 1)) for i in range(9)], dtype=np.float_
    )

    plt.bar(digits, msd_prob)

    ax.set_title(f"Histogram of n={n} trials")
    ax.set_xlabel("Most Significant Digit")
    ax.set_ylabel("Probability")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()

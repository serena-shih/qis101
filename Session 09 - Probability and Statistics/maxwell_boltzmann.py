#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

from __future__ import annotations

import typing
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi, exp

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def pdf(a : int) -> None:
    """Generates array representing PDF distribution at a"""
    xs : NDArray[np.float_] = np.linspace(0, 20, num=100, dtype=np.float_)
    P : NDArray[np.float_] = xs
    for i in range(len(P)):
        x : np.float_ = xs[i]
        P[i] = sqrt(2/pi) * (x**2 / a**3) * exp(-1 * x**2 / (2 * a**2))
    return P

def plot(ax : Axes) -> None:
    xs : NDArray[np.float_] = np.linspace(0, 20, num=100, dtype=np.float_)

    pdf1 : NDArray[np.float_] = pdf(1)
    pdf2 : NDArray[np.float_] = pdf(2)
    pdf5 : NDArray[np.float_] = pdf(5)

    ax.plot(xs, pdf1, color="red", label="a = 1")
    ax.plot(xs, pdf2, color="green", label="a = 2")
    ax.plot(xs, pdf5, color="blue", label="a = 5")

    ax.set_title("Maxwell-Boltzmann PDF Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")
    ax.legend()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
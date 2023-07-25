#!/usr/bin/env python3
"""werner_formula.py"""

from __future__ import annotations
import typing
import numpy as np
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(-3*np.pi, 3*np.pi, 1000)
    f1: NDArray[np.float_] = np.sin(0.8 * x)
    f2: NDArray[np.float_] = np.sin(0.5 * x)
    f3: NDArray[np.float_] = f1 * f2
    f4: NDArray[np.float_] = (np.cos(0.3 * x) - np.cos(1.3 * x)) / 2

    ax.plot(x, f1, label=r"$f_1(x) = sin(0.8x)$")
    ax.plot(x, f2, label=r"$f_2(x) = sin(0.5x)$")
    ax.plot(x, f3, label=r"$f_3(x) = f_1(x) + f_2(x)$")
    ax.plot(x, f4, linestyle='dotted', label=r"$f_4(x)=\frac{cos(0.3x)-cos(1.3x)}{2}$")

    ax.set_title("Werner's Formula")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
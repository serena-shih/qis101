#!/usr/bin/env python3
"""eulers_constant.py"""

import typing

import numpy as np
from scipy.integrate import quadrature as quad
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

def f(x: float) -> float:
    """Defines function used to estimate Euler's constant"""
    return np.log(np.log(1 / x))

def gamma() -> float:
    """Estimates Euler's constant"""
    return -1 * quad(f, 0, 1)[0]

def plot(ax: Axes) -> None:
    """Plots estimated Euler's constant and harmonic step function"""
    x: NDArray[np.float_] = np.linspace(0, 49)
    y: NDArray[np.float_] = gamma() + np.log(x + 1)

    h: NDArray[np.float_] = np.zeros(50)
    h[0] = 1
    for i in range(49):
        h[i+1] = h[i] + 1 / (i + 2)

    ax.plot(x, y, label=r"$\gamma + ln x$")
    ax.step(x, h, where="post", label="Harmonic numbers")
    ax.set_title("Euler's Constant and Harmonic Numbers")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
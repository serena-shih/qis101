#!/usr/bin/env python3
"""archimedes_spiral.py"""

from __future__ import annotations
import typing
import numpy as np
from scipy.integrate import quadrature as quad
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(x: float) -> float:
    """Defines Archimedean spiral function"""
    return np.sqrt(x**2 + 1)

def plot(ax: Axes) -> None:
    """Plots and calculates spiral function and arc length"""
    theta: NDArray[np.float_] = np.linspace(0, 8 * np.pi, num=1000)
    x: NDArray[np.float_] = theta * np.cos(theta)
    y: NDArray[np.float_] = theta * np.sin(theta)

    arc_len: float = quad(f, 0, 8 * np.pi)[0]

    ax.plot(x, y)
    ax.set_title(f"Arc length from 0 to 8pi = {arc_len:.5}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.set_aspect('equal')

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
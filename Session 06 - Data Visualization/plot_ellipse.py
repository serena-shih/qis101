#!/usr/bin/env python3
"""plot_ellipse.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

from math import sqrt

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot an ellipse of major axis length 100, minor axis length 50"""
    a : float = 100.0
    b : float = 50.0
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    radius : NDArray[np.float_] = []

    for angle in theta:
        r : np.float_ = (a*b)/sqrt((b*np.cos(angle))**2 + (a*np.sin(angle))**2)
        radius = np.append(radius, r)
 
    # Polar to Cartesian coordinate conversion using vectorized operations
    x: NDArray[np.float_] = []
    y: NDArray[np.float_] = []
    for i in range(len(theta)):
        x = np.append(x, radius[i] * np.cos(theta[i]))
    for i in range(len(theta)):
        y = np.append(y, radius[i] * np.sin(theta[i]))

    ax.plot(x, y)

    ax.set_title(r"$\frac{x^2}{100^2} + \frac{y^2}{50^2} = 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
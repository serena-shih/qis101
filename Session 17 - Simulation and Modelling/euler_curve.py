#!/usr/bin/env python3
"""euler_curve.py"""

from __future__ import annotations
import typing
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def x_f(u: np.float_) -> np.float_:
    return np.cos(u**2)

def y_f(u: np.float_) -> np.float_:
    return np.sin(u**2)

def arc_len_f(u: np.float_) -> np.float_:
    return np.sqrt((np.sin(u**2))**2 + (np.cos(u**2))**2)

def plot(ax: Axes) -> None:
    t: NDArray[np.float_] = np.linspace(0, 12.34, 1000)

    x: NDArray[np.float_] = np.asarray([])
    y: NDArray[np.float_] = np.asarray([])

    for u in t:
        x = np.append(x, quad(x_f, 0, u)[0])
        y = np.append(y, quad(y_f, 0, u)[0])

    # Calculate arc length
    arc_len: np.float_ = quad(arc_len_f, 0, 12.34)[0]

    ax.plot(x, y, color='black')

    ax.set_title(f"Euler Curve (Arc length = {arc_len:.4})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Display limit as t goes to +inf
    x_lim: np.float_ = np.sqrt(np.pi / 2) / 2
    y_lim: np.float_ = x_lim
    ax.plot([x_lim], [y_lim], color='green', marker='o', markersize=5)

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
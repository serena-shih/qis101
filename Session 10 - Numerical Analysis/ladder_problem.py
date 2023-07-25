#!/usr/bin/env python3
"""ladder_problem.py"""

from __future__ import annotations

import typing

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray
    from scipy.optimize import OptimizeResult

def ladder_len(theta : NDArray[np.float__]) -> NDArray[np.float_]:
    """Expression for ladder length function"""
    h1 : float = 2 / np.sin(theta)
    h2 : float = 1/np.cos(theta)
    return h1 + h2

# Referenced Dr. Biersach's code
def plot(ax : Axes):
    """Plot function to find maximum length of ladder"""
    theta : NDArray[np.float_] = np.linspace(0, np.pi / 2, num=1000)[1:-2]
    ladder_lens : NDArray[np.float_] = ladder_len(theta)

    ax.plot(theta, ladder_lens)

    ax.set_xlabel("Theta")
    ax.set_ylabel("Length in meters")

    res : OptimizeResult = scipy.optimize.minimize(ladder_len, np.pi / 4)
    min : NDArray[np.float_] = [res.x[0]]

    min_len : np.float = float(ladder_len(min))

    ax.set_title(f"Ladder length (maximized at {min_len:.4} meters)")

def main():
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
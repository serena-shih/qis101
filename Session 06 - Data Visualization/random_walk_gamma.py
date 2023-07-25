#!/usr/bin/env python3
"""random_walk_gamma.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def gamma(x : float):
    ans, err = quad(lambda t : t**(x-1)*(np.e)**(-t), 0, np.inf)
    return ans

def plot(ax: Axes) -> None:
    dimensions: NDArray[np.float_] = np.linspace(1.0, 25.0, 1000)
    distance: NDArray[np.float_] = []
    for d in dimensions:
        exp : float = (2*20000/d) * (gamma((d+1)/2) / gamma(d/2))**2
        distance = np.append(distance, exp)

    ax.plot(dimensions, distance)
    ax.set_title("Uniform Random Walk Expected Final Distances")
    ax.set_xlabel("Dimensions")
    ax.set_ylabel("Distance")


def main() -> None:
    plt.figure(__file__)    
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
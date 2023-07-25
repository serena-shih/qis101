#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations
import typing
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(a: NDArray[np.float_], b: NDArray[np.float_]) -> NDArray[np.complex_]:
    return abs(np.sin(a + b * 1j))

def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.float_] = np.linspace(-1, 1, 100)

    x, y = np.meshgrid(x, y)

    z: NDArray[np.complex_] = f(x, y)

    surf: Any = ax.plot_surface(x, y, z, 
                                cmap=cm.coolwarm, linewidth=0, antialiased=False)

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()

if __name__ == "__main__":
    main()
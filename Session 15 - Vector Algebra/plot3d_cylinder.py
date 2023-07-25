#!/usr/bin/env python3
"""plot3d_cylinder.py"""

from __future__ import annotations
import typing
import matplotlib.pyplot as plt
import numpy as np
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    """Plot 3D Cylinder"""
    u: NDArray[np.float_] = np.linspace(0, np.pi, 30)
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)

    x: NDArray[np.float_] = np.outer(np.ones_like(u), np.sin(v))
    y: NDArray[np.float_] = np.outer(np.ones_like(u), np.cos(v))
    z: NDArray[np.float_] = np.outer(np.cos(u), np.ones_like(v))

    ax.scatter(x, y, z)
    ax.plot_wireframe(x, y, z)
    # ax.plot_surface(x, y, z)

def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
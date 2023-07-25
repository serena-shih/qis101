#!/usr/bin/env python3
"""plot_trajectory.py"""

from __future__ import annotations
import typing
from pathlib import Path
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data: NDArray[np.float_] = np.genfromtxt(data_file, delimiter=",")

    t: NDArray[np.float_] = data[:, 0]
    h: NDArray[np.float_] = data[:, 1]

    ax.scatter(t, h, label="Actual", color="red", s=5)

    model: LinearRegression = LinearRegression().fit(t.reshape(-1, 1), h)
    slope: np.float_ = model.coef_[0]
    intercept: np.float_ = model.intercept_

    c: np.float_ = 29.97
    print(f"Velocity: {abs(slope)/c:.4} c")

    time_lived: np.float_ = 174_300
    impact_time: np.float_ = -1 * intercept / slope
    print(f"Height emitted: {(slope * (impact_time - time_lived) + intercept) / 100_000:.4} km")

    ax.plot(t, slope * t + intercept, label="Interpolation")
    ax.set_title("Cosmic Ray Trajectory")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Height (cm)")
    ax.legend()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
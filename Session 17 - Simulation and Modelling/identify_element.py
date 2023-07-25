#!/usr/bin/env python3
"""identify_element.py"""

from __future__ import annotations
import typing
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
if typing.TYPE_CHECKING:
    from numpy.typing import NDArray
    from matplotlib.axes import Axes

def c_to_k(x: np.float_) -> np.float_:
    """Convert Celsius to Kelvin"""
    return x + 273

def l_to_m3(x: np.float_) -> np.float_:
    """Convert liters to cubic meters"""
    return x / 1000

def f(a: np.float_, b: np.float_, t: np.float_) -> np.float_:
    """Defines linear regression function"""
    return a * t + b

def plot(ax: Axes) -> tuple[np.float_]:
    t: NDArray[np.float_] = c_to_k(np.asarray([-50, 0, 50, 100, 150]))
    v: NDArray[np.float_] = l_to_m3(np.asarray([11.6, 14, 16.2, 19.4, 21.8]))

    ax.scatter(t, v, label="Actual Points")

    model: LinearRegression = LinearRegression().fit(t.reshape(-1, 1), v)

    slope: np.float_ = model.coef_[0]
    intercept: np.float_ = model.intercept_

    x: NDArray[np.float_] = np.linspace(c_to_k(-50), c_to_k(150), 1000)
    y: NDArray[np.float_] = f(slope, intercept, x)

    ax.plot(x, y, label="Interpolation")

    ax.set_title(r"$T (^\circ K) \;\; vs \;\; V (m^3)$ (Argon gas)")
    ax.set_xlabel("T")
    ax.set_ylabel("V")
    ax.legend()

    return slope, intercept

def calc_mol(slp: np.float_, intcpt: np.float_, t: np.float_) -> np.float_:
    """Use Ideal Gas Law to calculate number of moles"""
    R: np.float_ = .0000820573
    return 2 * f(slp, intcpt, t) / (R * t)

def main() -> None:
    plt.figure(__file__)
    slp, intcpt = plot(plt.axes())
    n: np.float_ = calc_mol(slp, intcpt, 325)
    print(f"Number of moles is {n:.5}")
    mol_mass: np.float_ = 50 / n
    print(f"Molecular mass of the element is {mol_mass:.5} g/mol.")
    plt.show()

if __name__ == "__main__":
    main()
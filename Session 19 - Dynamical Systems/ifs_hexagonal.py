#!/usr/bin/env python3
"""ifs_hexagonal.py"""

from ifs import IteratedFunctionSystem
from pygame import Color
import numpy as np
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()

def plot_ifs(ss: SimpleScreen) -> None:
    iterations: int = 100_000
    x: float = 0
    y: float = 0
    clr: Color

    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)

def main() -> None:
    ifs.set_base_frame(0, 0, 30, 30)

    p: float = 1 / 6
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + 5*np.sqrt(3), Color("blue"), p)
    ifs.add_mapping(20, 15+5*np.sqrt(3), 15, 15, 10, 15 + 5*np.sqrt(3), Color("blue"), p)
    ifs.add_mapping(10, 15+5*np.sqrt(3), 15, 15, 5, 15, Color("blue"), p)
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - 5*np.sqrt(3), Color("blue"), p)
    ifs.add_mapping(10, 15-5*np.sqrt(3), 15, 15, 20, 15 - 5*np.sqrt(3), Color("blue"), p)
    ifs.add_mapping(20, 15-5*np.sqrt(3), 15, 15, 25, 15, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(world_rect=((0, 0), (30, 30)),
                      screen_size=(900, 900),
                      draw_function=plot_ifs,
                      title="IFS Hexagon")
    
    ss.show()

if __name__ == "__main__":
    main()
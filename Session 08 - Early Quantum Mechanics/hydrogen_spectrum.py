#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

def bohr():
    """Calculate hydrogen spectrum with Bohr's formula"""
    e : float = 1.602 * 10**(-19)
    m : float = 9.109 * 10**(-31)
    ep0 : float = 8.854 * 10**(-12)
    h : float = 6.626 * 10**(-34)
    c : float = 2.998 * 10**8

    e_0 : float = (e**4) * m / (8 * (ep0**2) * (h**2))

    print("Bohr Model for Hydrogen Spectral Lines")

    print("Pfund Series")
    # Below code taken from spectrum_bohr.py
    for init_orbit in range(6, 11):
        e_i: float = -e_0 / (init_orbit**2)
        e_f: float = -e_0 / 25
        wave_length: float = h * c / (e_i - e_f) * 1e9
        print(f"\t{init_orbit:>2} -> {5:>2}{wave_length:8.0f} nm")
    print()

    print("Humphreys Series")
    # Below code taken from spectrum_bohr.py
    for init_orbit in range(7, 12):
        e_i: float = -e_0 / (init_orbit**2)
        e_f: float = -e_0 / 36
        wave_length: float = h * c / (e_i - e_f) * 1e9
        print(f"\t{init_orbit:>2} -> {6:>2}{wave_length:8.0f} nm")
    print()
    return

def rydberg():
    """Calculate hydrogen spectrum with Rydberg's formula"""

    # Below code taken from spectrum_rydberg.py
    rydberg_constant: float = 1.0967757e7

    print("Rydberg Formula for Hydrogen Spectral Lines")

    print("Pfund Series")
    for j in range(6, 11):
        wave_length: float = (
            1 / (rydberg_constant * (1 / pow(5, 2) - 1 / pow(j, 2))) * 1e9
        )
        print(f"\t{j:>2} -> {5:>2}{wave_length:8.0f} nm")
    print()
    
    print("Humphreys Series")
    for j in range(7, 12):
        wave_length: float = (
            1 / (rydberg_constant * (1 / pow(6, 2) - 1 / pow(j, 2))) * 1e9
        )
        print(f"\t{j:>2} -> {6:>2}{wave_length:8.0f} nm")
    print()

def main():
    bohr()
    rydberg()

if __name__ == "__main__":
    main()
"""
VS Code debugger practice.

This script is intentionally broken, but it is designed to run far enough that
students can practice breakpoints, stepping through functions, and watching
variables change.

Run it with:

    python3 vscode_debug_spring.py

Suggested VS Code debugger practice:

1. Put a breakpoint on the first line inside main().
2. Start debugging.
3. Step over lines that assign variables.
4. Step into the functions below.
5. Watch variables such as k, mass, x, force, energy, period, forces, and
   energies.
6. Fix one bug at a time.
"""

import numpy as np


def spring_force(k, x):
    """Return the spring force in newtons."""
    # Bug: Hooke's law should have a minus sign.
    force = k * x
    return force


def spring_energy(k, x):
    """Return the spring potential energy in joules."""
    # Bug: this should use x**2.
    energy = 0.5 * k * x
    return energy


def spring_period(mass, k):
    """Return the period of a mass-spring oscillator in seconds."""
    # Bug: the ratio is upside down.
    period = 2 * np.pi * np.sqrt(k / mass)
    return period


def average(values):
    """Return the average of a list of values."""
    total = 0.0

    # Bug: this skips the last value.
    for i in range(len(values) - 1):
        total = total + values[i]

    return total / len(values)


def main():
    k = 20.0
    mass = 0.5
    displacements = [0.0, 0.05, 0.10, 0.15, 0.20]

    forces = []
    energies = []

    for x in displacements:
        force = spring_force(k, x)
        energy = spring_energy(k, x)

        forces.append(force)
        energies.append(energy)

    period = spring_period(mass, k)
    average_energy = average(energies)

    print("Spring debugging summary")
    print("k =", k, "N/m")
    print("mass =", mass, "kg")
    print("displacements =", displacements)
    print("forces =", forces)
    print("energies =", energies)
    print("period =", period, "s")
    print("average energy =", average_energy, "J")

    # Bug: index 5 does not exist for a list with 5 elements.
    print("last force =", forces[5], "N")


main()

"""
Broken physics debugging practice.

This file is supposed to contain errors. Run it with:

    python3 broken_physics.py

Fix one problem at a time. After each fix, run the file again and read the next
error message. Some problems are Python errors. Other problems are physics or
logic errors where the code runs but gives the wrong answer.
"""


# Goal 1: compute kinetic energy.
mass = "2.0"
speed = 3.0

kinetic_energy = 0.5 * mass * speed**2

print("kinetic energy =", kinetic_energy, "J")


# Goal 2: classify a temperature.
temperature = 295.0

if temperature > 290.0
    print("The sample is warm.")
else:
    print("The sample is cold.")


# Goal 3: compute force from mass and acceleration.
mass = 1.5
acceleration = 9.8

force = mas * acceleration

print("force =", force, "N")


# Goal 4: compute average speed from position and time data.
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]

average_speed = positions[-1] - positions[0] / times[-1] - times[0]

print("average speed =", average_speed, "m/s")


# Goal 5: print the last measured position.
print("last position =", positions[4], "m")


# Goal 6: compute spring force for several displacements.
spring_constant = 20.0
displacements = [0.1, -0.1, 0.2]
forces = []

for displacement in displacements:
spring_force = -spring_constant * displacement
    forces.append(spring_force)

print("spring forces =", forces)


# Goal 7: compute the average temperature.
temperatures = [289.0, 291.0, 293.0, 295.0]

average_temperature = sum(temperatures) / len(temperature)

print("average temperature =", average_temperature, "K")


# Goal 8: compute the period of a mass-spring oscillator.
import numpy as np


def spring_period(mass, spring_constant):
    """Return the period of a mass-spring oscillator."""
    period = 2 * np.pi * np.sqrt(spring_constant / mass)
    return period


period = spring_period(0.5, 20.0)

print("period =", period, "s")


# Goal 9: create a small table of measurements.
import pandas as pd

data = {
    "time_s": [0.0, 1.0, 2.0],
    "position_m": [0.0, 1.5],
}

df = pd.DataFrame(data)

print(df)


# Goal 10: plot position vs. time.
import matplotlib.pyplot as plt

plt.plot(time, positions, "o-")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Position vs. Time")
plt.show()

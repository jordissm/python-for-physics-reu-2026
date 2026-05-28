# Plotting

In this section, you will learn how to make plots with Matplotlib.

Plots are important in physics because they help us see patterns in data. A
table of numbers is useful, but a plot can make relationships much easier to
understand.

You will learn how to:

- make a simple plot
- label axes
- add a title and legend
- plot data from a `.dat` file
- save a plot as an image file

## Create a New Python File

1. Create a new file named `plotting.py`.
2. Run the file.

At first, nothing will happen because the file is empty.

## Import Matplotlib

Add this code to `plotting.py`:

```python
import matplotlib.pyplot as plt
```

The name `plt` is the standard nickname for `matplotlib.pyplot`.

## A First Plot

Add this code:

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]

plt.plot(times, positions)
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

Run the file. The plot should save in the directory where the script is run.

## Add Markers

The plot is easier to read if we show the data points:

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]

plt.plot(times, positions, 'o-', markersize=10)
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

The `"o-"` means "draw circles at the data points and connect them with a
line".

## Add Labels

A plot should tell the reader what is being shown.

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]

plt.plot(times, positions, "o-", markersize=6)
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Position vs. Time")
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

Axis labels should include units when possible.

## Plot More Than One Quantity

You can put more than one curve on the same plot.

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
position_a = [0.0, 1.2, 4.8, 10.8, 19.2]
position_b = [0.0, 2.0, 4.0, 6.0, 8.0]

plt.plot(times, position_a, "o-", label="accelerating", markersize=6)
plt.plot(times, position_b, "s-", label="constant speed", markersize=6)
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Two Motion Examples")
plt.legend()
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

The `label` values appear in the legend. The `plt.legend()` line tells
Matplotlib to show the legend.

## A Physics Example: Spring Force

Hooke's law is:

```text
F = -k*x
```

In Python:

```python
import matplotlib.pyplot as plt

spring_constant = 20.0
displacements = [-0.2, -0.1, 0.0, 0.1, 0.2]
forces = []

for x in displacements:
    force = -spring_constant * x
    forces.append(force)

plt.plot(displacements, forces, "o-", markersize=6)
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.savefig("force_vs_displacement.png")

print("Saved plot to force_vs_displacement.png")
```

The graph should be a straight line with a negative slope.

## Plot With NumPy

NumPy can create many evenly spaced values.

```python
import numpy as np
import matplotlib.pyplot as plt

spring_constant = 20.0
displacements = np.linspace(-0.2, 0.2, 100)
forces = -spring_constant * displacements

plt.plot(displacements, forces)
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.savefig("force_vs_displacement.png")

print("Saved plot to force_vs_displacement.png")
```

The line:

```python
displacements = np.linspace(-0.2, 0.2, 100)
```

creates 100 values from `-0.2` to `0.2`.

## Save a Plot

Use `plt.savefig` to save a plot as an image file.

```python
import numpy as np
import matplotlib.pyplot as plt

spring_constant = 20.0
displacements = np.linspace(-0.2, 0.2, 100)
forces = -spring_constant * displacements

plt.plot(displacements, forces)
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.title("Spring Force")
plt.savefig("spring_force.png")

print("Saved plot to spring_force.png")
```

After running the file, look for `spring_force.png` in the same folder as
`plotting.py`.

Saving figures is useful for reports, slides, and lab notebooks.

## Plot Data From a `.dat` File

The project section creates a data file named `spring_results.dat`. You can
read that file with pandas and plot the results.

Then use this code:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.dat", sep=r"\s+", comment="#")

plt.plot(df["displacement_m"], df["force_N"], "o-")
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.title("Spring Force From Data File")
plt.savefig("spring_force_from_data.png")

print("Saved plot to spring_force_from_data.png")
```

The column names in the code must match the column names in the `.dat` file.
The option `sep=r"\s+"` tells pandas that columns are separated by spaces. The
option `comment="#"` tells pandas to ignore lines that start with `#`.

## Plot Energy From the Same `.dat` File

You can make a second plot using a different column.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.dat", sep=r"\s+", comment="#")

plt.plot(df["displacement_m"], df["energy_J"], "o-")
plt.xlabel("displacement (m)")
plt.ylabel("energy (J)")
plt.title("Spring Potential Energy")
plt.savefig("spring_energy_from_data.png")

print("Saved plot to spring_energy_from_data.png")
```

The energy should be smallest at `x = 0` and positive for both positive and
negative displacement.

## Make Two Plots in One Figure

Use subplots to show related plots together.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.dat", sep=r"\s+", comment="#")

fig, axes = plt.subplots(2, 1)

axes[0].plot(df["displacement_m"], df["force_N"], "o-")
axes[0].set_ylabel("force (N)")
axes[0].set_title("Spring Results")

axes[1].plot(df["displacement_m"], df["energy_J"], "o-")
axes[1].set_xlabel("displacement (m)")
axes[1].set_ylabel("energy (J)")

plt.tight_layout()
plt.savefig("spring_results.png")

print("Saved plot to spring_results.png")
```

The line `plt.tight_layout()` helps prevent labels from overlapping.

## Common Beginner Mistakes

### Mismatched list lengths

The x-values and y-values must have the same length.

This will cause an error:

```python
times = [0.0, 1.0, 2.0]
positions = [0.0, 1.0]

plt.plot(times, positions)
```

### Misspelling a column name

If your data file has a column named `force_N`, this works:

```python
df["force_N"]
```

This does not:

```python
df["force"]
```

### Forgetting to save

Use `plt.savefig(...)` to write the plot to an image file:

```python
plt.savefig("figure.png")
```

## Practice

Try these in `plotting.py`.

1. Use NumPy to create 50 time values from `0` to `5` seconds.
2. Compute two position lists or arrays:

   ```text
   position_a = 1.5*t
   position_b = 0.5*t**2
   ```

3. Plot both positions on the same axes with different markers or line styles.
4. Add axis labels with units, a title, and a legend.
5. Save the plot as `two_positions.png`.
6. Create a second figure that plots the difference
   `position_b - position_a` vs. time.
7. Add a horizontal line at `0` with:

   ```python
   plt.axhline(0)
   ```

8. Save the second figure as `position_difference.png`.

## Challenge

Use the `.dat` file from the project section.

1. Run the spring project to create `spring_results.dat`.
2. Read the data file with pandas.
3. Make a plot of force vs. displacement.
4. Make a plot of energy vs. displacement.
5. Add a third plot that shows the force magnitude, `abs(force_N)`, vs.
   displacement.
6. Put all three plots in one figure using subplots.
7. Add axis labels to every subplot.
8. Save the figure as `spring_summary.png`.

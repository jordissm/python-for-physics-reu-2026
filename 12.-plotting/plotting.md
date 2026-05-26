# Plotting

In this section, you will learn how to make plots with Matplotlib.

Plots are important in physics because they help us see patterns in data. A
table of numbers is useful, but a plot can make relationships much easier to
understand.

You will learn how to:

- make a simple plot
- label axes
- add a title and legend
- plot data from a CSV file
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
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

Run the file. The plot should save in the directory where the
script is ran.

## Add Markers

The plot is easier to read if we show the data points:

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]

plt.plot(times, positions)
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

The `"o-"` means "draw circles at the data points and connect them with a
line".

## Add Labels and a Title

A plot should tell the reader what is being shown.

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]

plt.plot(times, positions, "o-")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Position vs. Time")
plt.show()
```

Axis labels should include units when possible.

## Plot More Than One Quantity

You can put more than one curve on the same plot.

```python
import matplotlib.pyplot as plt

times = [0.0, 1.0, 2.0, 3.0, 4.0]
position_a = [0.0, 1.2, 4.8, 10.8, 19.2]
position_b = [0.0, 2.0, 4.0, 6.0, 8.0]

plt.plot(times, position_a, "o-", label="accelerating")
plt.plot(times, position_b, "s-", label="constant speed")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Two Motion Examples")
plt.legend()
plt.show()
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

plt.plot(displacements, forces, "o-")
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.title("Spring Force")
plt.show()
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
plt.title("Spring Force")
plt.show()
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
plt.show()
```

After running the file, look for `spring_force.png` in the same folder as
`plotting.py`.

Saving figures is useful for reports, slides, and lab notebooks.

## Plot Data From a CSV File

The project section creates a CSV file named `spring_results.csv`. You can read
that file with pandas and plot the results.

If you do not already have `spring_results.csv`, create one with this content:

```text
displacement_m,force_N,energy_J
-0.2,4.0,0.4
-0.1,2.0,0.1
0.0,0.0,0.0
0.1,-2.0,0.1
0.2,-4.0,0.4
```

Then use this code:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.csv")

plt.plot(df["displacement_m"], df["force_N"], "o-")
plt.xlabel("displacement (m)")
plt.ylabel("force (N)")
plt.title("Spring Force From CSV")
plt.show()
```

The column names in the code must match the column names in the CSV file.

## Plot Energy From the Same CSV File

You can make a second plot using a different column.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.csv")

plt.plot(df["displacement_m"], df["energy_J"], "o-")
plt.xlabel("displacement (m)")
plt.ylabel("energy (J)")
plt.title("Spring Potential Energy")
plt.show()
```

The energy should be smallest at `x = 0` and positive for both positive and
negative displacement.

## Make Two Plots in One Figure

Use subplots to show related plots together.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spring_results.csv")

fig, axes = plt.subplots(2, 1)

axes[0].plot(df["displacement_m"], df["force_N"], "o-")
axes[0].set_ylabel("force (N)")
axes[0].set_title("Spring Results")

axes[1].plot(df["displacement_m"], df["energy_J"], "o-")
axes[1].set_xlabel("displacement (m)")
axes[1].set_ylabel("energy (J)")

plt.tight_layout()
plt.savefig("spring_results.png")
plt.show()
```

The line `plt.tight_layout()` helps prevent labels from overlapping.

## Common Beginner Mistakes

### Forgetting `plt.show()`

If you do not call `plt.show()`, the plot window may not appear.

```python
plt.plot(x, y)
plt.show()
```

### Mismatched list lengths

The x-values and y-values must have the same length.

This will cause an error:

```python
times = [0.0, 1.0, 2.0]
positions = [0.0, 1.0]

plt.plot(times, positions)
```

### Misspelling a column name

If your CSV has a column named `force_N`, this works:

```python
df["force_N"]
```

This does not:

```python
df["force"]
```

### Saving after showing

For beginner scripts, save before `plt.show()`:

```python
plt.savefig("figure.png")
plt.show()
```

## Practice

Try these in `plotting.py`.

1. Create a list of times.
2. Create a list of positions.
3. Plot position vs. time with markers.
4. Add axis labels with units.
5. Add a title.
6. Save the plot as `position_vs_time.png`.
7. Create a spring force plot using Hooke's law.
8. Save it as `spring_force.png`.

## Challenge

Use the CSV file from the project section.

1. Run the spring project to create `spring_results.csv`.
2. Read the CSV file with pandas.
3. Make a plot of force vs. displacement.
4. Make a plot of energy vs. displacement.
5. Put both plots in one figure using subplots.
6. Save the figure as `spring_summary.png`.

# Libraries

In this section, you will learn how to import Python libraries.

A library is a collection of code that other people have already written by other people in which they have defined variables, functions, classes that you can use. Python libraries let us do numerical calculations, make plots, fit
data, and work with tables without writing everything from scratch. There is a library for everything, some libraries can help you collect data from searching through many web pages, some libraries can help you edit pdfs or even video/audio files.

In this bootcamp, we will use:

- NumPy for arrays and numerical calculations
- SciPy for scientific tools such as curve fitting
- Matplotlib for plotting
- pandas for table-like data

## Before You Start

Install the required libraries by typing the following into your terminal (bottom part of vs code)

```bash
pip install numpy
pip install scipy
pip install Matplotlib
pip install pandas
```

If you are not sure whether the libraries installed, run the following on the terminal in VS code:

```bash
python3 -m pip list
```

You should see `numpy`, `scipy`, `matplotlib`, and `pandas` in the list.

## Create a New Python File

1. Create a new file named `libraries.py`.
2. Add this code to `libraries.py`:

```python
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd

print("Libraries imported successfully.")
```

Run the file:

You should see:

```text
Libraries imported successfully.
```

The word `import` tells Python to load a library.

The phrase `as np` gives NumPy a shorter nickname. These nicknames are common (but you can use any, such as `import numpy as math_library`):

- `numpy as np`
- `matplotlib.pyplot as plt`
- `pandas as pd`

## NumPy Arrays

NumPy is useful for numerical data. A NumPy array is similar to a list, but it is
designed for math.

```python
import numpy as np

times = np.array([0.0, 1.0, 2.0, 3.0])
positions = np.array([0.0, 2.0, 4.5, 7.5])

print(times)
print(positions)
```

NumPy can do arithmetic on entire arrays:

```python
velocities = positions / times

print(velocities)
```

This example will produce a warning for the first value because it divides by
zero. Warnings are not always fatal errors, but they are worth reading.

A safer example is:

```python
times = np.array([1.0, 2.0, 3.0])
positions = np.array([2.0, 4.5, 7.5])

velocities = positions / times

print(velocities)
```

## Useful NumPy Functions

NumPy includes functions for common calculations:

```python
import numpy as np

temperatures = np.array([290.0, 292.5, 295.0, 291.5])

print("mean =", np.mean(temperatures))
print("minimum =", np.min(temperatures))
print("maximum =", np.max(temperatures))
print("standard deviation =", np.std(temperatures))
```

The mean is the average. The standard deviation gives a sense of how spread out
the values are.

## SciPy Example

SciPy includes many tools for scientific computing. Here is a small example
using a linear fit.

```python
import numpy as np
from scipy.optimize import curve_fit

def line(x, slope_input, intercept_input):
    return slope_input * x + intercept_input

times = np.array([0.0, 1.0, 2.0, 3.0])
positions = np.array([0.1, 2.1, 4.0, 6.2])

parameters, covariance = curve_fit(line, times, positions)

slope = parameters[0]
intercept = parameters[1]

print("slope =", slope)
print("intercept =", intercept)
```

For position vs. time data, the slope is the fitted velocity.

Do not worry about `covariance` yet. We will focus on the fitted parameters.

## Matplotlib Plot

Matplotlib makes plots.

```python
import numpy as np
import matplotlib.pyplot as plt

times = np.array([0.0, 1.0, 2.0, 3.0])
positions = np.array([0.1, 2.1, 4.0, 6.2])

plt.plot(times, positions)
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.savefig("position_vs_time.png")

print("Saved plot to position_vs_time.png")
```

When you run this code, a plot will be saved in your system.

## pandas DataFrames

pandas is useful for table-like data.

```python
import pandas as pd

data = {
    "time_s": [0.0, 1.0, 2.0, 3.0],
    "position_m": [0.1, 2.1, 4.0, 6.2],
}

df = pd.DataFrame(data)

print(df)
print(df["position_m"])
print(df["position_m"].mean())
```

A DataFrame is like a small spreadsheet inside Python.

## Common Beginner Mistakes

### Importing before installing

If you see an error like this:

```text
ModuleNotFoundError: No module named 'numpy'
```

the library is probably not installed in your active virtual environment.

### Misspelling the library name

This works:

```python
import numpy as np
```

This does not:

```python
import numppy as np
```

### Forgetting the nickname

If you import NumPy as `np`, use `np` later:

```python
import numpy as np

values = np.array([1, 2, 3])
```

## Practice

Try these in `libraries.py`.

1. Import NumPy as `np`.
2. Create a NumPy array of five mass values.
3. Print the mean mass.
4. Import Matplotlib as `plt`.
5. Plot time on the x-axis and position on the y-axis.
6. Import pandas as `pd`.
7. Create a DataFrame with columns for time and position.
8. Print the DataFrame.

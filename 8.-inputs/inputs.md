# Inputs

## Command-Line Inputs

Very often, you dont want to modify your script everytime you run it. Instead you want to be able to specify some variables when you call the script from the terminal:

For example you can pass the variables `2.0` and `3.0` into a Python script by writing the following code and then using the `sys` library in the file:

```bash
python3 inputs.py 2.0 3.0
```

## Reading Command-Line Inputs With `sys.argv`

The command line inputs `2.0` and `3.0` above are passed to your Python code under the variable name: `sys.argv`.

Try running the following:

```python
import sys

print(sys.argv)
```

Run Python from the terminal by saying

```bash
python3 inputs.py 2.0 3.0
```

You should see something like:

```text
['inputs.py', '2.0', '3.0']
```

The first value is the script name. The values after that are the inputs.

Command-line inputs are strings, and need to be converted to numbers for use. You can convert a string into a float by using the command float(). For example `float("6.0")` turns the string `"6"` (which cannot be used to multiple another number since it is a string) into a float type.

## A Physics Example With Command-Line Inputs

This program computes kinetic energy using command-line inputs:

```python
import sys

mass = float(sys.argv[1])
speed = float(sys.argv[2])

kinetic_energy = 0.5 * mass * speed**2

print("mass =", mass, "kg")
print("speed =", speed, "m/s")
print("kinetic energy =", kinetic_energy, "J")
```

Run:

```bash
python3 inputs.py 2.0 3.0
```

You should see:

```text
mass = 2.0 kg
speed = 3.0 m/s
kinetic energy = 9.0 J
```

try inputting a different set of 2 inputs

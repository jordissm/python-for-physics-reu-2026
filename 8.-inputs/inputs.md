# Inputs

## Command-Line Inputs

Very often, you do not want to modify your script every time you run it.
Instead, you want to specify some variables when you call the script from the
terminal.

For example, you can pass the variables `2.0` and `3.0` into a Python script by
running:

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

Command-line inputs are strings, and need to be converted to numbers for use.
You can convert a string into a float by using `float()`. For example,
`float("6.0")` turns the string `"6.0"` into a number.

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

Try inputting a different set of 2 inputs.

## Named Command-Line Inputs With `argparse`

The `sys.argv` method works, but it has one important weakness: the order of the
inputs matters. If you accidentally switch the order of `mass` and `speed`, the
program will still run, but the calculation will be wrong.

The `argparse` library lets you give names to your command-line inputs. It also
prints helpful instructions if the user forgets an input.

Try replacing the code in `inputs.py` with this:

```python
import argparse

parser = argparse.ArgumentParser(description="Compute kinetic energy.")

parser.add_argument("--mass", type=float, required=True,
                    help="mass in kg")
parser.add_argument("--speed", type=float, required=True,
                    help="speed in m/s")

args = parser.parse_args()

kinetic_energy = 0.5 * args.mass * args.speed**2

print("mass =", args.mass, "kg")
print("speed =", args.speed, "m/s")
print("kinetic energy =", kinetic_energy, "J")
```

Run:

```bash
python3 inputs.py --mass 2.0 --speed 3.0
```

You should see:

```text
mass = 2.0 kg
speed = 3.0 m/s
kinetic energy = 9.0 J
```

The command-line inputs now have names:

- `--mass`
- `--speed`

The order no longer matters. These two commands give the same result:

```bash
python3 inputs.py --mass 2.0 --speed 3.0
python3 inputs.py --speed 3.0 --mass 2.0
```

## What `add_argument` Means

Each `parser.add_argument(...)` line describes one command-line input.

```python
parser.add_argument("--mass", type=float, required=True,
                    help="mass in kg")
```

This line says:

- the input name is `--mass`
- the value should be converted to a float
- the input is required
- the help message should say `"mass in kg"`

If you run:

```bash
python3 inputs.py
```

Python will print a usage message because the required inputs are missing.

You can also ask for help directly:

```bash
python3 inputs.py --help
```

## Reading Several Values With `argparse`

Sometimes you want one command-line option to accept several values. The
argument `nargs="+"` means "read one or more values."

```python
import argparse

parser = argparse.ArgumentParser(description="Compute kinetic energies.")

parser.add_argument("--mass", type=float, required=True,
                    help="mass in kg")
parser.add_argument("--speeds", type=float, nargs="+", required=True,
                    help="speeds in m/s")

args = parser.parse_args()

for speed in args.speeds:
    kinetic_energy = 0.5 * args.mass * speed**2
    print("speed =", speed, "m/s")
    print("kinetic energy =", kinetic_energy, "J")
```

Run:

```bash
python3 inputs.py --mass 2.0 --speeds 1.0 2.0 3.0
```

This pattern is useful when a physics calculation needs a list of positions,
times, speeds, or displacements.

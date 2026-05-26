# Project: Spring Calculator With CLI and Text Output

In this project, you will write a Python script that computes useful quantities
for a spring and saves the results to a plain text file.

This project uses the main ideas from the bootcamp:

- variables
- libraries
- command-line inputs
- lists
- conditional statements
- loops
- functions
- text file output
- debugging habits

The physics is based on Hooke's law:

```text
F = -k*x
```

where:

- `F` is the spring force in newtons
- `k` is the spring constant in N/m
- `x` is the displacement from equilibrium in meters

You will also compute spring potential energy:

```text
U = 0.5*k*x**2
```

and the period of a mass on a spring:

```text
T = 2*pi*sqrt(m/k)
```

## Project Goal

Your script should:

1. Accept inputs from the command line.
2. Compute spring force and spring potential energy for several displacements.
3. Compute the period of the mass-spring oscillator.
4. Save the results to a text file.
5. Print a short summary to the terminal.

## Create a New Python File

1. Create a new file named `spring_project.py`.
2. Run the file.

At first, nothing will happen because the file is empty.

## Start With Imports

At the top of `spring_project.py`, add:

```python
import argparse
import math
```

These libraries do different jobs:

- `argparse` reads command-line inputs
- `math` provides `math.pi` and `math.sqrt`

## Write the Physics Functions

Add these functions:

```python
def spring_force(k, x):
    """Return the spring force in newtons."""
    return -k * x


def spring_energy(k, x):
    """Return the spring potential energy in joules."""
    return 0.5 * k * x**2


def spring_period(mass, k):
    """Return the period of a mass-spring oscillator in seconds."""
    return 2 * math.pi * math.sqrt(mass / k)
```

## Read Command-Line Inputs

Add this function:

```python
def parse_arguments():
    parser = argparse.ArgumentParser(description="Compute spring quantities.")

    parser.add_argument("--spring-constant", type=float, required=True,
                        help="spring constant in N/m")
    parser.add_argument("--mass", type=float, required=True,
                        help="mass in kg")
    parser.add_argument("--displacements", type=float, nargs="+", required=True,
                        help="displacements in m")
    parser.add_argument("--output", default="spring_results.txt",
                        help="text output file")

    return parser.parse_args()
```

This lets the user run the script with direct command-line values:

```bash
python3 spring_project.py --spring-constant 20 --mass 0.5 --displacements -0.2 -0.1 0.0 0.1 0.2 --output spring_results.txt
```

## Validate the Inputs

Add this function:

```python
def inputs_are_valid(k, mass, displacements):
    if k <= 0:
        print("Spring constant must be positive.")
        return False

    if mass <= 0:
        print("Mass must be positive.")
        return False

    if len(displacements) == 0:
        print("At least one displacement is required.")
        return False

    return True
```

Validation is a debugging tool. It catches bad inputs before the calculation
starts.

## Compute the Results

Add this function:

```python
def compute_results(k, displacements):
    results = []

    for x in displacements:
        force = spring_force(k, x)
        energy = spring_energy(k, x)

        row = {
            "displacement_m": x,
            "force_N": force,
            "energy_J": energy,
        }

        results.append(row)

    return results
```

This function creates a list of dictionaries. Each dictionary represents one
set of calculated values.

## Write the Text Output File

Add this function:

```python
def write_text_file(filename, k, mass, period, results):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Spring calculation results\n")
        file.write("==========================\n")
        file.write("\n")
        file.write(f"spring constant = {k} N/m\n")
        file.write(f"mass = {mass} kg\n")
        file.write(f"period = {period} s\n")
        file.write("\n")
        file.write("displacement_m    force_N    energy_J\n")

        for row in results:
            x = row["displacement_m"]
            force = row["force_N"]
            energy = row["energy_J"]
            file.write(f"{x}    {force}    {energy}\n")
```

The output file will contain a short summary followed by one line for each
displacement.

## Put the Program Together

Add the `main` function:

```python
def main():
    args = parse_arguments()

    k = args.spring_constant
    mass = args.mass
    displacements = args.displacements

    if not inputs_are_valid(k, mass, displacements):
        return

    period = spring_period(mass, k)
    results = compute_results(k, displacements)

    write_text_file(args.output, k, mass, period, results)

    print("Spring calculation complete.")
    print("spring constant =", k, "N/m")
    print("mass =", mass, "kg")
    print("period =", round(period, 3), "s")
    print("wrote output to", args.output)


main()
```

## Run With CLI Inputs

Run:

```bash
python3 spring_project.py --spring-constant 20 --mass 0.5 --displacements -0.2 -0.1 0.0 0.1 0.2 --output spring_results.txt
```

You should see:

```text
Spring calculation complete.
spring constant = 20.0 N/m
mass = 0.5 kg
period = 0.993 s
wrote output to spring_results.txt
```

Open `spring_results.txt`. It should contain:

```text
Spring calculation results
==========================

spring constant = 20.0 N/m
mass = 0.5 kg
period = 0.9934588265796101 s

displacement_m    force_N    energy_J
-0.2    4.0    0.4000000000000001
-0.1    2.0    0.10000000000000002
0.0    -0.0    0.0
0.1    -2.0    0.10000000000000002
0.2    -4.0    0.4000000000000001
```

## Debugging Checks

Try these checks:

1. Run the script without any inputs:

   ```bash
   python3 spring_project.py
   ```

   It should print a helpful command-line usage message.

2. Run with a negative spring constant:

   ```bash
   python3 spring_project.py --spring-constant -20 --mass 0.5 --displacements 0.1
   ```

   It should print a helpful validation message.

3. Test a known force:

   ```text
   if k = 20 and x = 0.1, then F = -2 N
   ```

4. Test a known energy:

   ```text
   if k = 20 and x = 0.1, then U = 0.1 J
   ```

5. Check that the output file has one result line for each displacement.

## Practice Changes

After the basic program works, try these changes:

1. Round the text output values to 3 decimal places.
2. Add a warning if any displacement has magnitude greater than `1.0` meter.
3. Add the maximum force magnitude to the terminal summary.
4. Add the average energy to the text output file.
5. Add a Matplotlib plot of force vs. displacement.

# Project: Spring Calculator With CLI, YAML, and CSV Output

In this project, you will write a Python script that computes useful quantities
for a spring and saves the results to a CSV file.

This project uses the main ideas from the bootcamp:

- variables
- libraries
- command-line inputs
- YAML input files
- lists
- conditional statements
- loops
- functions
- CSV output files
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
2. Accept inputs from a YAML file.
3. Compute spring force and spring potential energy for several displacements.
4. Compute the period of the mass-spring oscillator.
5. Save the results to a CSV file.
6. Print a short summary to the terminal.

## Create a New Python File

1. Create a new file named `spring_project.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Make sure the required libraries are installed:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Run the file from the terminal with:

   ```bash
   python3 spring_project.py
   ```

At first, nothing will happen because the file is empty.

## Create a YAML Input File

Create a file named `spring_input.yaml` in the same folder as
`spring_project.py`:

```yaml
spring_constant: 20.0
mass: 0.5
displacements:
  - -0.2
  - -0.1
  - 0.0
  - 0.1
  - 0.2
```

This file stores the physics inputs for the calculation.

## Start With Imports

At the top of `spring_project.py`, add:

```python
import argparse
import csv

import numpy as np
import yaml
```

These libraries do different jobs:

- `argparse` reads command-line inputs
- `csv` writes CSV files
- `numpy` provides `np.pi` and `np.sqrt`
- `yaml` reads the YAML input file

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
    return 2 * np.pi * np.sqrt(mass / k)
```

## Read Command-Line Inputs

Add this function:

```python
def parse_arguments():
    parser = argparse.ArgumentParser(description="Compute spring quantities.")

    parser.add_argument("--config", help="YAML input file")
    parser.add_argument("--output", default="spring_results.csv", help="CSV output file")
    parser.add_argument("--spring-constant", type=float, help="spring constant in N/m")
    parser.add_argument("--mass", type=float, help="mass in kg")
    parser.add_argument("--displacements", type=float, nargs="+", help="displacements in m")

    return parser.parse_args()
```

This lets the user run the script in two ways.

With a YAML file:

```bash
python3 spring_project.py --config spring_input.yaml --output spring_results.csv
```

Or with direct command-line values:

```bash
python3 spring_project.py --spring-constant 20 --mass 0.5 --displacements -0.2 -0.1 0.0 0.1 0.2 --output spring_results.csv
```

## Read the YAML File

Add this function:

```python
def read_yaml(filename):
    with open(filename, "r") as file:
        config = yaml.safe_load(file)

    return config
```

The YAML file becomes a dictionary with keys such as `"spring_constant"`,
`"mass"`, and `"displacements"`.

## Choose Inputs From CLI or YAML

Add this function:

```python
def get_inputs(args):
    if args.config is not None:
        config = read_yaml(args.config)
    else:
        config = {}

    if args.spring_constant is not None:
        k = args.spring_constant
    else:
        k = config.get("spring_constant")

    if args.mass is not None:
        mass = args.mass
    else:
        mass = config.get("mass")

    if args.displacements is not None:
        displacements = args.displacements
    else:
        displacements = config.get("displacements")

    return k, mass, displacements
```

This function uses command-line values if they are provided. Otherwise, it looks
for values in the YAML file.

## Validate the Inputs

Add this function:

```python
def inputs_are_valid(k, mass, displacements):
    if k is None or mass is None or displacements is None:
        print("Missing input. Use CLI values or provide a YAML config file.")
        return False

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

This function creates a list of dictionaries. Each dictionary represents one row
of output.

## Write the CSV Output File

Add this function:

```python
def write_csv(filename, results):
    fieldnames = ["displacement_m", "force_N", "energy_J"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
```

The file will have three columns:

```text
displacement_m,force_N,energy_J
```

## Put the Program Together

Add the `main` function:

```python
def main():
    args = parse_arguments()
    k, mass, displacements = get_inputs(args)

    if not inputs_are_valid(k, mass, displacements):
        return

    period = spring_period(mass, k)
    results = compute_results(k, displacements)

    write_csv(args.output, results)

    print("Spring calculation complete.")
    print("spring constant =", k, "N/m")
    print("mass =", mass, "kg")
    print("period =", round(period, 3), "s")
    print("wrote output to", args.output)


main()
```

## Full Program

Your full `spring_project.py` should look like this:

```python
import argparse
import csv

import numpy as np
import yaml


def spring_force(k, x):
    """Return the spring force in newtons."""
    return -k * x


def spring_energy(k, x):
    """Return the spring potential energy in joules."""
    return 0.5 * k * x**2


def spring_period(mass, k):
    """Return the period of a mass-spring oscillator in seconds."""
    return 2 * np.pi * np.sqrt(mass / k)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Compute spring quantities.")

    parser.add_argument("--config", help="YAML input file")
    parser.add_argument("--output", default="spring_results.csv", help="CSV output file")
    parser.add_argument("--spring-constant", type=float, help="spring constant in N/m")
    parser.add_argument("--mass", type=float, help="mass in kg")
    parser.add_argument("--displacements", type=float, nargs="+", help="displacements in m")

    return parser.parse_args()


def read_yaml(filename):
    with open(filename, "r") as file:
        config = yaml.safe_load(file)

    return config


def get_inputs(args):
    if args.config is not None:
        config = read_yaml(args.config)
    else:
        config = {}

    if args.spring_constant is not None:
        k = args.spring_constant
    else:
        k = config.get("spring_constant")

    if args.mass is not None:
        mass = args.mass
    else:
        mass = config.get("mass")

    if args.displacements is not None:
        displacements = args.displacements
    else:
        displacements = config.get("displacements")

    return k, mass, displacements


def inputs_are_valid(k, mass, displacements):
    if k is None or mass is None or displacements is None:
        print("Missing input. Use CLI values or provide a YAML config file.")
        return False

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


def write_csv(filename, results):
    fieldnames = ["displacement_m", "force_N", "energy_J"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    args = parse_arguments()
    k, mass, displacements = get_inputs(args)

    if not inputs_are_valid(k, mass, displacements):
        return

    period = spring_period(mass, k)
    results = compute_results(k, displacements)

    write_csv(args.output, results)

    print("Spring calculation complete.")
    print("spring constant =", k, "N/m")
    print("mass =", mass, "kg")
    print("period =", round(period, 3), "s")
    print("wrote output to", args.output)


main()
```

## Run With YAML Input

Run:

```bash
python3 spring_project.py --config spring_input.yaml --output spring_results.csv
```

You should see:

```text
Spring calculation complete.
spring constant = 20.0 N/m
mass = 0.5 kg
period = 0.992 s
wrote output to spring_results.csv
```

Open `spring_results.csv`. It should contain:

```text
displacement_m,force_N,energy_J
-0.2,4.0,0.4000000000000001
-0.1,2.0,0.10000000000000002
0.0,-0.0,0.0
0.1,-2.0,0.10000000000000002
0.2,-4.0,0.4000000000000001
```

## Run With Direct CLI Inputs

Run:

```bash
python3 spring_project.py --spring-constant 20 --mass 0.5 --displacements -0.2 -0.1 0.0 0.1 0.2 --output spring_results_cli.csv
```

This should produce a second CSV file named `spring_results_cli.csv`.

## Debugging Checks

Try these checks:

1. Run the script without any inputs:

   ```bash
   python3 spring_project.py
   ```

   It should print a helpful missing-input message.

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

## Practice Changes

After the basic program works, try these changes:

1. Add the period to a second output file named `spring_summary.txt`.
2. Round the CSV output values to 3 decimal places.
3. Add a warning if any displacement has magnitude greater than `1.0` meter.
4. Add another YAML key named `experiment_name` and print it in the summary.
5. Add a Matplotlib plot of force vs. displacement.

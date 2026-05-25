# Inputs

In this section, you will learn how to let a user type information into a Python
program.

Input is useful when you want a program to ask for values instead of editing the
code every time. For example, a program might ask for a mass, a velocity, or a
temperature.

The first tool is `input`, which asks the user a question while the program is
running. Later in this lesson, you will also learn two other input styles:

- command-line inputs, which are values typed after the script name
- YAML inputs, which are values stored in a small configuration file

## Create a New Python File

1. Create a new file named `inputs.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Run the file from the terminal with:

   ```bash
   python3 inputs.py
   ```

At first, nothing will happen because the file is empty.

## Your First Input

Add this code to `inputs.py`:

```python
name = input("What is your name? ")

print("Hello,", name)
```

Run the file:

```bash
python3 inputs.py
```

Python will pause and wait for you to type something. Type your name and press
Enter.

## Input Is Text

The value returned by `input` is always a string, even if the user types a
number.

Try this:

```python
value = input("Enter a number: ")

print(value)
print(type(value))
```

The output will show `<class 'str'>`. A string is text.

## Converting Input to a Number

If you want to do math with input, convert it to a number.

Use `float` for decimal values:

```python
mass_text = input("Enter mass in kg: ")
mass = float(mass_text)

print("mass =", mass, "kg")
print("twice the mass =", 2 * mass, "kg")
```

This can be written more compactly:

```python
mass = float(input("Enter mass in kg: "))

print("mass =", mass, "kg")
```

Use `int` for whole numbers:

```python
number_of_trials = int(input("Enter number of trials: "))

print("trials =", number_of_trials)
```

For physics calculations, `float` is usually the better choice.

## A Physics Example: Kinetic Energy

Kinetic energy is:

```text
K = 0.5 * m * v**2
```

In Python:

```python
mass = float(input("Enter mass in kg: "))
speed = float(input("Enter speed in m/s: "))

kinetic_energy = 0.5 * mass * speed**2

print("kinetic energy =", kinetic_energy, "J")
```

Run the file several times with different values.

## A Physics Example: Unit Conversion

This program converts Celsius to Kelvin:

```python
celsius = float(input("Enter temperature in Celsius: "))

kelvin = celsius + 273.15

print("temperature =", kelvin, "K")
```

Try entering:

- `0`
- `20`
- `100`

## Combining Input With Conditionals

Input becomes more useful when combined with `if` statements.

```python
temperature = float(input("Enter temperature in K: "))

if temperature < 273.15:
    print("Below freezing")
elif temperature < 310.0:
    print("Moderate temperature")
else:
    print("High temperature")
```

The program responds differently depending on what the user types.

## Command-Line Inputs

Sometimes you do not want the program to stop and ask questions one at a time.
Instead, you may want to give the values when you run the script.

For example:

```bash
python3 inputs.py 2.0 3.0
```

The values `2.0` and `3.0` are command-line inputs.

## Reading Command-Line Inputs With `sys.argv`

Python stores command-line inputs in `sys.argv`.

Replace the contents of `inputs.py` with:

```python
import sys

print(sys.argv)
```

Run:

```bash
python3 inputs.py 2.0 3.0
```

You should see something like:

```text
['inputs.py', '2.0', '3.0']
```

The first value is the script name. The values after that are the inputs.

Command-line inputs are strings, just like values from `input`.

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

## Checking the Number of Command-Line Inputs

If the user forgets an input, `sys.argv[1]` or `sys.argv[2]` may not exist. That
causes an error.

Add a check:

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python3 inputs.py MASS SPEED")
else:
    mass = float(sys.argv[1])
    speed = float(sys.argv[2])

    kinetic_energy = 0.5 * mass * speed**2

    print("kinetic energy =", kinetic_energy, "J")
```

Run it incorrectly:

```bash
python3 inputs.py 2.0
```

Then run it correctly:

```bash
python3 inputs.py 2.0 3.0
```

## YAML Input Files

For programs with several inputs, command-line inputs can become hard to read.
A configuration file is often cleaner.

YAML is a simple file format for storing named values.

Create a new file named `spring_input.yaml`:

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

This file stores:

- one spring constant
- one mass
- a list of displacements

## Reading YAML in Python

To read YAML, use the `yaml` library. This comes from the `PyYAML` package in
`requirements.txt`.

Make sure your libraries are installed:

```bash
python3 -m pip install -r requirements.txt
```

Then use this code in `inputs.py`:

```python
import yaml

with open("spring_input.yaml", "r") as file:
    config = yaml.safe_load(file)

print(config)
print(config["spring_constant"])
print(config["mass"])
print(config["displacements"])
```

Run:

```bash
python3 inputs.py
```

YAML input gives you a dictionary. A dictionary stores values using names called
keys. In this example, the keys are `"spring_constant"`, `"mass"`, and
`"displacements"`.

## A Physics Example With YAML

This program reads spring inputs from YAML and computes forces:

```python
import yaml

with open("spring_input.yaml", "r") as file:
    config = yaml.safe_load(file)

k = config["spring_constant"]
mass = config["mass"]
displacements = config["displacements"]

print("spring constant =", k, "N/m")
print("mass =", mass, "kg")

for x in displacements:
    force = -k * x
    print("x =", x, "m", "force =", force, "N")
```

YAML is useful when you want to run the same program many times with different
settings.

## Common Beginner Mistakes

### Forgetting to convert input

This does not do the physics calculation you probably want:

```python
mass = input("Enter mass in kg: ")
speed = input("Enter speed in m/s: ")

kinetic_energy = 0.5 * mass * speed**2
```

`mass` and `speed` are strings here. Convert them with `float`.

### Typing text when Python expects a number

This code expects a number:

```python
mass = float(input("Enter mass in kg: "))
```

If the user types `hello`, Python cannot convert it to a number and will show an
error.

### Missing spaces in prompts

This prompt is easier to read:

```python
mass = float(input("Enter mass in kg: "))
```

The space before the final quotation mark keeps the user's answer from running
into the prompt text.

### Forgetting that command-line inputs are strings

This does not do a numerical calculation:

```python
import sys

mass = sys.argv[1]
speed = sys.argv[2]
kinetic_energy = 0.5 * mass * speed**2
```

Convert command-line inputs with `float` or `int`.

### Running a script from the wrong folder

If Python cannot find your YAML file, check that you are running the script from
the folder that contains the YAML file.

Use:

```bash
pwd
```

## Practice

Try these in `inputs.py`.

1. Ask the user for a distance in meters.
2. Ask the user for a time in seconds.
3. Compute speed using:

   ```text
   speed = distance / time
   ```

4. Print the speed with units of `m/s`.
5. Ask the user for a radius.
6. Compute the area of a circle using:

   ```text
   area = pi * radius**2
   ```

7. Print the area.
8. Modify your program so it can compute kinetic energy from command-line
   inputs:

   ```bash
   python3 inputs.py 2.0 3.0
   ```

9. Create a YAML file named `spring_input.yaml`.
10. Read the YAML file and print each displacement.

## Challenge

Write a small program that asks for:

- initial position `x0`
- initial velocity `v0`
- acceleration `a`
- time `t`

Then compute:

```text
x = x0 + v0*t + 0.5*a*t**2
```

Print the final position with units.

Then write a second version that receives those same four values from the
command line.

Then write a third version that reads those values from a YAML file.

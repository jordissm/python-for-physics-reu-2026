# Output Files

In this section, you will learn how to save calculation results to a file.

So far, most of our programs have used `print` to show results in the terminal.
That is useful, but terminal output disappears easily. For real work, we often
want to save results so we can:

- look at them later
- share them with someone else
- plot them in another program
- keep a record of an experiment or calculation

Python can write output files such as plain text files and CSV files.

## Create a New Python File

1. Create a new file named `output.py`.
2. Add this code to `output.py`:

```python
message = "Python wrote this file.\n"

with open("results.txt", "w") as file:
    file.write(message)
```

Run the file. You should see a new file named `results.txt`
in the same folder as `output.py`. Open it in VS Code. It should contain:

```text
Python wrote this file.
```

The `\n` means "new line".

## What `with open(...)` Means

This line opens a file:

```python
with open("results.txt", "w") as file:
```

The `"w"` means write mode. Write mode creates the file if it does not exist.
If the file already exists, write mode replaces the old contents.

The indented lines under `with open(...)` are allowed to write to the file.
After the indented block ends, Python closes the file automatically.

## Writing Calculation Results

Now write a physics calculation to a text file:

```python
mass = 2.0
speed = 3.0
kinetic_energy = 0.5 * mass * speed**2

with open("kinetic_energy.txt", "w") as file:
    file.write("Kinetic energy calculation\n")
    file.write("mass = " + str(mass) + " kg\n")
    file.write("speed = " + str(speed) + " m/s\n")
    file.write("kinetic energy = " + str(kinetic_energy) + " J\n")
```

Run the file and open `kinetic_energy.txt`.

The `str(...)` function converts a number to text so it can be written to the
file.

## A Cleaner Way: f-strings

An f-string makes it easier to combine text and variables.

```python
mass = 2.0
speed = 3.0
kinetic_energy = 0.5 * mass * speed**2

with open("kinetic_energy.txt", "w") as file:
    file.write("Kinetic energy calculation\n")
    file.write(f"mass = {mass} kg\n")
    file.write(f"speed = {speed} m/s\n")
    file.write(f"kinetic energy = {kinetic_energy} J\n")
```

The `f` before the quotation mark tells Python to fill in values inside `{}`.

You can also round values:

```python
file.write(f"kinetic energy = {kinetic_energy:.3f} J\n")
```

The `:.3f` means "print this number with 3 digits after the decimal point".

## Writing Many Results

Lists and loops are useful when writing many results.

```python
mass = 2.0
speeds = [1.0, 2.0, 3.0, 4.0]

with open("energies.txt", "w") as file:
    file.write("speed_m_per_s kinetic_energy_J\n")

    for speed in speeds:
        kinetic_energy = 0.5 * mass * speed**2
        file.write(f"{speed} {kinetic_energy}\n")
```

Open `energies.txt`. It should contain a small table.

## Writing a CSV File

A CSV file is a comma-separated values file. CSV files are useful because many
programs can open them, including spreadsheet programs and pandas.

```python
mass = 2.0
speeds = [1.0, 2.0, 3.0, 4.0]

with open("energies.csv", "w") as file:
    file.write("speed_m_per_s,kinetic_energy_J\n")

    for speed in speeds:
        kinetic_energy = 0.5 * mass * speed**2
        file.write(f"{speed},{kinetic_energy}\n")
```

Open `energies.csv` in VS Code. You should see:

```text
speed_m_per_s,kinetic_energy_J
1.0,1.0
2.0,4.0
3.0,9.0
4.0,16.0
```

## A Physics Example: Spring Output File

This example computes spring force and spring potential energy for several
displacements, then writes the results to a CSV file.

```python
spring_constant = 20.0
displacements = [-0.2, -0.1, 0.0, 0.1, 0.2]

with open("spring_results.csv", "w") as file:
    file.write("displacement_m,force_N,energy_J\n")

    for x in displacements:
        force = -spring_constant * x
        energy = 0.5 * spring_constant * x**2

        file.write(f"{x},{force},{energy}\n")
```

Run the file and open `spring_results.csv`.

This example uses:

- variables
- a list
- a loop
- physics formulas
- file output

## Reading the File Back

You can read a text file with `"r"` mode.

```python
with open("spring_results.csv", "r") as file:
    contents = file.read()

print(contents)
```

This prints the file contents back to the terminal.

Reading the file back is a good debugging check. It helps confirm that the file
contains what you expected.

## Appending to a File

Write mode `"w"` replaces old file contents. Append mode `"a"` adds to the end
of a file.

```python
with open("log.txt", "a") as file:
    file.write("Ran the spring calculation.\n")
```

Run this several times and open `log.txt`. Each run adds another line.

Use append mode when you want to keep old output.

## Common Beginner Mistakes

### Forgetting `\n`

Without `\n`, output can run together on one line:

```python
file.write("first line")
file.write("second line")
```

Use:

```python
file.write("first line\n")
file.write("second line\n")
```

### Forgetting to convert numbers to strings

This causes an error:

```python
file.write(kinetic_energy)
```

Use an f-string:

```python
file.write(f"{kinetic_energy}\n")
```

### Looking in the wrong folder

Python writes the output file in the folder where the script is running. In VS
Code, this is usually the folder shown in the terminal.

Check your current folder with:

```bash
pwd
```

### Accidentally replacing a file

Write mode `"w"` replaces old contents:

```python
with open("results.txt", "w") as file:
```

Append mode `"a"` keeps old contents and adds new output:

```python
with open("results.txt", "a") as file:
```

## Practice

Try these in `output.py`.

1. Ask the user for a mass.
2. Ask the user for three speeds.
3. Store the speeds in a list.
4. Compute kinetic energy for each speed.
5. Write the speed and kinetic energy values to `kinetic_energies.csv`.
6. Include a header line:

   ```text
   speed_m_per_s,kinetic_energy_J
   ```

7. Open the CSV file in VS Code and check the results.

## Challenge

Write a program that asks for:

- spring constant `k`
- number of displacement values
- each displacement value

Then write a file named `spring_output.csv` with columns:

```text
displacement_m,force_N,energy_J
```

Use these formulas:

```text
force = -k*x
energy = 0.5*k*x**2
```

After writing the file, read it back and print its contents to the terminal.

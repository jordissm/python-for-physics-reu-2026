# Loops

In this section, you will learn how to repeat code.

Loops are useful when you want to do the same kind of work many times, such as:

- printing every value in a list
- computing a result for every measurement
- repeating a calculation for many times
- building up a new list of results

The two main loop tools in Python are `for` loops and `while` loops.

## Create a New Python File

1. Create a new file named `loops.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Run the file from the terminal with:

   ```bash
   python3 loops.py
   ```

At first, nothing will happen because the file is empty.

## A First `for` Loop

Add this code to `loops.py`:

```python
temperatures = [290.0, 292.5, 295.0, 291.5]

for temperature in temperatures:
    print(temperature)
```

Run the file:

```bash
python3 loops.py
```

You should see each temperature printed on its own line.

The loop reads naturally:

```text
for each temperature in temperatures, print the temperature
```

## Indentation Matters

The indented lines belong to the loop.

```python
temperatures = [290.0, 292.5, 295.0]

for temperature in temperatures:
    print("temperature =", temperature)
    print("recorded")

print("done")
```

The first two `print` lines run once for each temperature. The final `print`
line is not indented, so it runs once after the loop is finished.

## Looping Over a Range

Use `range` when you want to loop over a sequence of integers.

```python
for i in range(5):
    print(i)
```

The output is:

```text
0
1
2
3
4
```

Just like list indexes, `range(5)` starts at `0` and stops before `5`.

## Building a List With a Loop

You can start with an empty list and append values inside a loop.

```python
times = [0.0, 1.0, 2.0, 3.0]
velocities = []

for time in times:
    velocity = 2.0 * time
    velocities.append(velocity)

print(velocities)
```

This creates a velocity value for each time value.

## A Physics Example: Position at Many Times

For constant acceleration:

```text
x = x0 + v0*t + 0.5*a*t**2
```

In Python:

```python
times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = []

x0 = 0.0
v0 = 2.0
a = 1.5

for t in times:
    x = x0 + v0 * t + 0.5 * a * t**2
    positions.append(x)

print(positions)
```

Run the file. Then change `v0` or `a` and run it again.

## Looping With Indexes

Sometimes you need the index of each value.

```python
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]

for i in range(len(times)):
    print("time =", times[i], "position =", positions[i])
```

The expression `len(times)` gives the number of values in the list.

## `enumerate`

Python also has a helpful tool called `enumerate`.

```python
positions = [0.0, 2.0, 4.5, 7.5]

for index, position in enumerate(positions):
    print(index, position)
```

`enumerate` gives both the index and the value.

## A First `while` Loop

A `while` loop repeats as long as a condition is `True`.

```python
count = 0

while count < 5:
    print(count)
    count = count + 1
```

The line `count = count + 1` is important. Without it, the loop would never
stop.

## Common Beginner Mistakes

### Forgetting the colon

Loop lines end with a colon:

```python
for value in values:
    print(value)
```

### Forgetting to indent

The code inside the loop must be indented:

```python
for value in values:
    print(value)
```

### Creating an infinite loop

This loop never stops:

```python
count = 0

while count < 5:
    print(count)
```

The value of `count` never changes, so the condition stays `True`.

If a program seems stuck, press Ctrl+C in the terminal to stop it.

## Practice

Try these in `loops.py`.

1. Create a list named `masses`.
2. Use a `for` loop to print each mass.
3. Create a list named `velocities`.
4. Use a loop to compute kinetic energy for each velocity:

   ```text
   kinetic_energy = 0.5 * mass * velocity**2
   ```

5. Store the kinetic energies in a new list.
6. Print the new list.
7. Use `range` to print the numbers from `0` to `9`.

## Challenge

Create this list:

```python
times = [0.0, 0.5, 1.0, 1.5, 2.0]
```

Use a loop to compute the height of a falling object at each time:

```text
y = y0 - 0.5*g*t**2
```

Use:

```python
y0 = 10.0
g = 9.8
```

Store the heights in a list and print the list.

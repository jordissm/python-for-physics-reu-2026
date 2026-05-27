# Lists

In this section, you will learn how to store several values in one variable.

A list is useful when you have a collection of related values, such as:

- several time measurements
- several position measurements
- several temperatures
- several particle names
- several results from an experiment

So far, most of our variables have stored one value at a time. Lists let us keep
many values together.

## Create a New Python File

1. Create a new file named `lists.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Run the file from the terminal with:

   ```bash
   python lists.py
   ```

At first, nothing will happen because the file is empty.

## Your First List

Add this code to `lists.py`:

```python
temperatures = [290.0, 292.5, 295.0, 291.5]

print(temperatures)
```

Run the file:

```bash
python lists.py
```

You should see:

```text
[290.0, 292.5, 295.0, 291.5]
```

The square brackets tell Python that this is a list. Each value in the list is
called an element.

## Lists Can Store Different Types of Values

A list can store numbers:

```python
times = [0.0, 1.0, 2.0, 3.0]
```

A list can store strings:

```python
particles = ["electron", "proton", "neutron"]
```

A list can even store booleans:

```python
passed_checks = [True, True, False, True]
```

For most scientific work, we usually keep one kind of value in a list. For
example, a list of times or a list of positions.

## Getting One Value From a List

Use an index to get one element from a list.

```python
positions = [0.0, 1.5, 4.0, 7.5]

print(positions[0])
print(positions[1])
print(positions[2])
print(positions[3])
```

Python starts counting at `0`, not `1`.

That means:

- `positions[0]` is the first element
- `positions[1]` is the second element
- `positions[2]` is the third element
- `positions[3]` is the fourth element

This is called zero-based indexing. It feels strange at first, but it becomes
normal with practice.

## Changing One Value

You can replace one element in a list:

```python
positions = [0.0, 1.5, 4.0, 7.5]

positions[1] = 2.0

print(positions)
```

The output should be:

```text
[0.0, 2.0, 4.0, 7.5]
```

Only the element at index `1` changed.

## Finding the Length of a List

Use `len` to find out how many elements are in a list:

```python
temperatures = [290.0, 292.5, 295.0, 291.5]

print(len(temperatures))
```

The output should be:

```text
4
```

The last index is always one less than the length. For this list, the length is
`4`, so the last index is `3`.

## Adding Values to a List

Use `.append()` to add one value to the end of a list:

```python
measurements = []

measurements.append(1.2)
measurements.append(1.5)
measurements.append(1.4)

print(measurements)
```

The output should be:

```text
[1.2, 1.5, 1.4]
```

The line `measurements = []` creates an empty list.

## Useful List Calculations

Python has some built-in functions that work on lists of numbers:

```python
temperatures = [290.0, 292.5, 295.0, 291.5]

print("number of measurements =", len(temperatures))
print("lowest temperature =", min(temperatures))
print("highest temperature =", max(temperatures))
print("sum of temperatures =", sum(temperatures))
print("average temperature =", sum(temperatures) / len(temperatures))
```

Run the code and check the output.

The average is calculated as:

```text
average = sum of values / number of values
```

## A Physics Example: Average Speed

Suppose you measure position at several times:

```python
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]
```

The average speed between the first and last measurement is:

```text
average speed = change in position / change in time
```

In Python:

```python
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]

start_time = times[0]
end_time = times[3]

start_position = positions[0]
end_position = positions[3]

average_speed = (end_position - start_position) / (end_time - start_time)

print("average speed =", average_speed, "m/s")
```

Run the file. Then change the final position and run it again.

## Getting the Last Value

Python has a shortcut for getting the last element in a list:

```python
positions = [0.0, 2.0, 4.5, 7.5]

print(positions[-1])
```

The index `-1` means "the last element".

You can use this to rewrite the average speed example:

```python
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]

average_speed = (positions[-1] - positions[0]) / (times[-1] - times[0])

print("average speed =", average_speed, "m/s")
```

## Slicing a List

A slice gets part of a list:

```python
positions = [0.0, 2.0, 4.5, 7.5, 11.0]

print(positions[0:3])
print(positions[2:5])
```

The slice `positions[0:3]` includes indexes `0`, `1`, and `2`. It stops before
index `3`.

This "stop before the end index" rule is common in Python.

## Checking Whether a Value Is in a List

Use `in` to check whether a list contains a value:

```python
particles = ["electron", "proton", "neutron"]

if "proton" in particles:
    print("The list contains a proton.")
```

You can also use `not in`:

```python
particles = ["electron", "proton", "neutron"]

if "muon" not in particles:
    print("No muon is listed.")
```

This combines lists with conditional statements.

## Common Beginner Mistakes

### Forgetting that Python starts counting at zero

For this list:

```python
values = [10, 20, 30]
```

The first value is `values[0]`, not `values[1]`.

### Using an index that does not exist

This list has three elements:

```python
values = [10, 20, 30]
```

The valid indexes are `0`, `1`, and `2`.

This will cause an error:

```python
print(values[3])
```

### Forgetting commas

List elements must be separated by commas:

```python
values = [1, 2, 3]
```

This is not the same thing:

```python
values = [1 2 3]
```

## Practice

Try these in `lists.py`.

1. Create a list named `masses` with at least four mass values.
2. Print the first mass.
3. Print the last mass using `masses[-1]`.
4. Print the number of masses using `len(masses)`.
5. Print the smallest and largest mass using `min` and `max`.
6. Create a list named `velocities`.
7. Compute the average of the velocities using `sum(velocities) / len(velocities)`.
8. Create a list named `particle_names`.
9. Use an `if` statement to check whether `"electron"` is in `particle_names`.

## Challenge

Create two lists:

```python
times = [0.0, 1.0, 2.0, 3.0, 4.0]
positions = [0.0, 1.2, 4.8, 10.8, 19.2]
```

Write code that computes the average speed between the first measurement and the
last measurement.

Then write code that computes the average speed between the second measurement
and the fourth measurement.

Remember that Python starts counting at zero.

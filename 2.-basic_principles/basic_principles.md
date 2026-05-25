# Basic Principles

In this section, you will practice the basic building blocks of Python:

- comments
- variables
- arithmetic
- strings
- booleans
- simple output with `print`

The goal is not to memorize every detail. The goal is to get comfortable typing
small pieces of code, running them, reading the output, and making small changes.

## Create a New Python File

1. Create a new file named `basic_principles.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Run the file from the terminal with:

   ```bash
   python basic_principles.py
   ```

At first, nothing will happen because the file is empty. That is okay.

## Comments

Comments are notes for humans. Python ignores them when the program runs.

Add this to `basic_principles.py`:

```python
# This is my first basic Python practice file.
# Lines that start with # are comments.
```

Run the file again:

```bash
python basic_principles.py
```

There should still be no output. Comments explain code, but they do not print
anything.

## Printing Values

Use `print` when you want Python to show something in the terminal.

Add this below your comments:

```python
print("Basic principles")
print("Python is running")
```

Run the file again. You should see:

```text
Basic principles
Python is running
```

## Variables

A variable is a name that stores a value. In physics, we often use names like
`time`, `distance`, `mass`, and `velocity`.

Add this code:

```python
time = 3.0
velocity = 12.0
distance = velocity * time

print(distance)
```

Run the file. Python should print:

```text
36.0
```

Python does the arithmetic using the values stored in the variables.

## Printing Labels

A number by itself is not always easy to understand. Add a label:

```python
print("distance =", distance)
```

This prints both text and the value of `distance`.

You can also include units:

```python
print("distance =", distance, "meters")
```

## Basic Arithmetic

Python can do the arithmetic you expect from a calculator:

```python
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** b =", a ** b)
```

The symbol `**` means "to the power of". For example, `10 ** 3` means
`10` cubed.

## A Physics Example: Constant Acceleration

For motion with constant acceleration, the position can be written as:

```text
x = x0 + v0*t + 0.5*a*t**2
```

In Python:

```python
x0 = 0.0
v0 = 5.0
a = 2.0
t = 4.0

x = x0 + v0 * t + 0.5 * a * t**2

print("position =", x, "meters")
```

Run the file and check the result. Then change `t` to a different value and run
it again.

## Strings

A string is text. Strings use quotation marks:

```python
name = "Ada"
course = "Python for Physics"

print(name)
print(course)
print(name, "is learning", course)
```

Strings are useful for labels, messages, filenames, and any data that should be
treated as text.

## Booleans

A boolean is either `True` or `False`.

```python
temperature = 295.0
is_room_temperature = temperature > 290.0

print(is_room_temperature)
```

The expression `temperature > 290.0` asks a question. Python answers with
`True` or `False`.

Try changing `temperature` to `250.0` and run the file again.

## Common Beginner Mistakes

### Capitalization matters

These are three different variable names:

```python
mass = 1.0
Mass = 2.0
MASS = 3.0
```

Try to use lowercase names like `mass`, `velocity`, and `time`.

### Quotation marks matter

This prints text:

```python
print("mass")
```

This prints the value stored in the variable named `mass`:

```python
print(mass)
```

### Order matters

You must create a variable before using it:

```python
speed = distance / time
```

This only works if `distance` and `time` already have values.

## Practice

Try these in `basic_principles.py`.

1. Create variables named `mass` and `acceleration`.
2. Compute force using:

   ```text
   force = mass * acceleration
   ```

3. Print the force with units of newtons.
4. Change the mass and acceleration values and run the file again.
5. Create variables named `radius` and `pi`.
6. Compute the area of a circle using:

   ```text
   area = pi * radius**2
   ```

7. Print the area.

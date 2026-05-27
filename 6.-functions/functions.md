# Functions

In this section, you will learn how to write your own functions.

A function is a named block of code that does one job. Functions help you:

- reuse code
- organize programs
- avoid copying and pasting the same calculation
- make physics formulas easier to read

You have already used built-in functions such as `print`, `len`, `sum`, `min`,
and `max`. Now you will define your own.

## Create a New Python File

1. Create a new file named `functions.py`.
2. Add this code to `functions.py`:

```python
def say_hello():
    print("Hello from a function.")

say_hello()
```

Run the file. You should see:

```text
Hello from a function.
```

The line starting with `def` defines the function. The final line calls the
function.

Defining a function does not run it. A function runs only when you call it.

## Parameters

Functions can receive information through parameters.

```python
def greet(name):
    print("Hello,", name)

greet("Ada")
greet("Grace")
```

Here, `name` is a parameter. Each time we call `greet`, we pass in a different
value.

## Returning Values

A function can send a value back using `return`.

```python
def square(x):
    return x**2

result = square(4)

print(result)
```

The output should be:

```text
16
```

Use `return` when a function should calculate a value for the rest of the
program to use.

## A Physics Example: Kinetic Energy

Kinetic energy is:

```text
K = 0.5 * m * v**2
```

As a function:

```python
def kinetic_energy(mass, speed):
    energy = 0.5 * mass * speed**2
    return energy

energy1 = kinetic_energy(2.0, 3.0)
energy2 = kinetic_energy(2.0, 5.0)

print("energy1 =", energy1, "J")
print("energy2 =", energy2, "J")
```

The function lets us reuse the same formula with different values.

## A Physics Example: Constant Acceleration

```python
def position_constant_acceleration(x0, v0, a, t):
    x = x0 + v0 * t + 0.5 * a * t**2
    return x

position = position_constant_acceleration(0.0, 2.0, 1.5, 4.0)

print("position =", position, "m")
```

Function names can be longer when that makes the code clearer.

## Functions and Lists

Functions can work with lists.

```python
def average(values):
    return sum(values) / len(values)

temperatures = [290.0, 292.5, 295.0, 291.5]

print("average temperature =", average(temperatures))
```

This is useful because average is a calculation we might need many times.

## Functions and Loops

You can call a function inside a loop.

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed**2

mass = 2.0
speeds = [1.0, 2.0, 3.0, 4.0]
energies = []

for speed in speeds:
    energy = kinetic_energy(mass, speed)
    energies.append(energy)

print(energies)
```

This combines functions, lists, and loops.

## Docstrings

A docstring is a short description inside a function.

```python
def kinetic_energy(mass, speed):
    """Return kinetic energy in joules."""
    return 0.5 * mass * speed**2
```

Docstrings help other people understand what your function is supposed to do.
They also help future you.

## Common Beginner Mistakes

### Forgetting to call the function

This defines a function but does not run it:

```python
def say_hello():
    print("hello")
```

This runs it:

```python
say_hello()
```

### Forgetting `return`

This prints a value but does not return it:

```python
def square(x):
    print(x**2)
```

This returns the value:

```python
def square(x):
    return x**2
```

### Mixing up parameters and arguments

In this function, `mass` and `speed` are parameters:

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed**2
```

In this function call, `2.0` and `3.0` are arguments:

```python
kinetic_energy(2.0, 3.0)
```

## Practice

Try these in `functions.py`.

1. Write a function named `force` that takes `mass` and `acceleration`.
2. The function should return `mass * acceleration`.
3. Call the function with at least two different sets of values.
4. Write a function named `celsius_to_fahrenheit`.
5. The function should return `celsius * 9 / 5 + 32`.
6. Write a function named `average_speed`.
7. The function should take `start_position`, `end_position`, `start_time`, and
   `end_time`.
8. The function should return the average speed.

## Challenge

Write a function named `height` that takes `y0`, `v0`, `g`, and `t`.

It should return:

```text
y = y0 + v0*t - 0.5*g*t**2
```

Then use a loop to call your function for each time in this list:

```python
times = [0.0, 0.5, 1.0, 1.5, 2.0]
```

Store the heights in a list and print the list.

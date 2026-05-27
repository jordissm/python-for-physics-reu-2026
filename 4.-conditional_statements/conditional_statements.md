# Conditional Statements

In this section, you will learn how to make a Python program choose between
different actions.

Conditional statements let a program ask questions like:

- Is this value positive?
- Is this temperature above a threshold?
- Has an object reached the ground?
- Should we print one message or another?

The main tools are `if`, `elif`, and `else`.

## Create a New Python File

1. Create a new file named `conditional_statements.py`.
2. Add this code to `conditional_statements.py`:

```python
temperature = 295.0

if temperature > 290.0:
    print("The sample is warm.")
```

Run the file, after which you should see:

```terminal
The sample is warm.
```

The line `temperature > 290.0` is a *condition*. Python checks whether the
condition is `True` or `False`.

If the condition is `True`, Python runs the indented code below the `if`
statement.

## Indentation Matters

In Python, indentation is part of the code. The spaces at the beginning of a
line tell Python which lines belong inside the `if` statement.

This works:

```python
temperature = 295.0

if temperature > 290.0:
    print("The sample is warm.")
    print("Check the cooling system.")
```

Both `print` lines are indented, so both lines belong to the `if` statement.

This does something different:

```python
temperature = 295.0

if temperature > 290.0:
    print("The sample is warm.")
print("This line always prints.")
```

The final `print` line is not indented, so it runs whether the condition is
`True` or `False`.

## `else`

Use `else` when you want one thing to happen if the condition is `True` and a
different thing to happen if the condition is `False`.

```python
temperature = 280.0

if temperature > 290.0:
    print("The sample is warm.")
else:
    print("The sample is not warm.")
```

Run the file. Then change `temperature` to `300.0` and run it again.

## `elif`

Use `elif` when you want to check more than two possibilities. `elif` means
"else if".

```python
temperature = 295.0

if temperature < 273.15:
    print("Below freezing")
elif temperature < 310.0:
    print("Moderate temperature")
else:
    print("High temperature")
```

Python checks the conditions from top to bottom. It runs the first block where
the condition is `True`, then skips the rest.

Try changing `temperature` to:

- `250.0`
- `295.0`
- `350.0`

Run the file after each change.

## Comparison Operators

Conditions often use comparison operators:

```python
x = 5

print(x == 5)
print(x != 5)
print(x > 3)
print(x < 3)
print(x >= 5)
print(x <= 4)
```

The output will be a set of `True` and `False` values.

Here is what the comparison operators mean:

- `==` means equal to
- `!=` means not equal to
- `>` means greater than
- `<` means less than
- `>=` means greater than or equal to
- `<=` means less than or equal to

Be careful with `=` and `==`.

```python
mass = 2.0
```

This stores the value `2.0` in the variable `mass`.

```python
mass == 2.0
```

This asks whether `mass` is equal to `2.0`.

## Combining Conditions

You can combine conditions with `and` and `or`.

```python
temperature = 295.0
pressure = 1.0

if temperature > 290.0 and pressure < 2.0:
    print("The experiment is in the target range.")
```

With `and`, both conditions must be `True`.

```python
temperature = 250.0
pressure = 5.0

if temperature < 260.0 or pressure > 4.0:
    print("Warning: check the experiment.")
```

With `or`, at least one condition must be `True`.

## A Physics Example: Has the Object Hit the Ground?

Suppose an object moves vertically. We can use a conditional statement to check
whether its height is above or below the ground.

```python
y0 = 10.0
v0 = 2.0
g = 9.8
t = 2.0

y = y0 + v0 * t - 0.5 * g * t**2

print("height =", y, "meters")

if y > 0:
    print("The object is still above the ground.")
else:
    print("The object has reached or passed the ground.")
```

Run the file. Then change `t` to a few different values and run it again.

## A Physics Example: Classifying Speed

This example classifies the speed of an object.

```python
speed = 12.0

if speed == 0:
    print("The object is at rest.")
elif speed < 5:
    print("The object is moving slowly.")
elif speed < 20:
    print("The object is moving at a moderate speed.")
else:
    print("The object is moving quickly.")
```

Try changing `speed` to:

- `0`
- `2`
- `12`
- `30`

## Common Beginner Mistakes

### Forgetting the colon

An `if`, `elif`, or `else` line must end with a colon:

```python
if speed > 10:
    print("fast")
```

### Using `=` instead of `==`

Use `==` when asking whether two values are equal:

```python
if speed == 0:
    print("at rest")
```

### Indenting inconsistently

Python expects the lines inside the same block to have the same indentation:

```python
if speed > 10:
    print("fast")
    print("measure again")
```

VS Code can help with indentation. If something looks shifted left or right,
check the spacing carefully.

## Practice

Try these in a new blank `conditional_statements.py`.

1. Create a variable named `TIME` and assign it the value `0`.
2. Create a variable named `SPEED_A` and assign it the value `5.0`.
3. Create a variable named `SPEED_B` and assign it the value `-2.0`.
4. Create a variable named `POSITION_A`, using the formula given by `POSITION_A = TIME * SPEED_A`.
5. Create a variable named `POSITION_B` using the formula given by `POSITION_B = TIME * SPEED_B`.
6. Print a message that shows the distance between both positions.
7. Print a message that says "Particles are far apart" when the distance between the positions is larger than `10 m`.
8. Print a message that says "Particles are close together" when the distance between the positions is smaller than `10 m` but larger than `2 m`.
9. Print a message that says "Particles are very close together" when the distance between the positions is smaller than `2 m`.
10. Run the script.
11. Change the values of `TIME` and see how it affects the output.

## Challenge

Write a small program that checks whether a projectile is above the ground,
exactly at the ground, or below the ground.

Use this starting point:

```python
y0 = 5.0
v0 = 8.0
g = 9.8
t = 1.0

y = y0 + v0 * t - 0.5 * g * t**2
```

Your program should print:

- `"above ground"` if `y > 0`
- `"at ground level"` if `y == 0`
- `"below ground"` if `y < 0`

Because decimal arithmetic is not always exact, it is usually better to check
whether a value is close to zero instead of exactly equal to zero.
We will learn more about this later.

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

The line `temperature > 290.0` is a *condition*. Python first evaluates the condition to be either true or false. If the condition is `True`, Python runs the indented code below the `if`
statement. Try the following code:

```python
temperature = 295.0

print(temperature > 290.0)
print(temperature < 290.0)
print(temperature == 290.0)
```

You should get the following result:

```text
True
False
False
```
Python reads >,< and == as an instruction to evaluate the relative sizes of the LHS and the RHS, and evaluates it as either 'True' or 'False'. just as the '+' sign takes in two inputs and evaluates their sum. Why are there two '=' signs? It is because python understands one '=' sign to already mean, set the temperature variable to the value 290.0, which will overwrite the earlier value of 290.0. You can try running it with one '=' sign to understand the behaviour.So python is executing the code one step at a time. Step one, replace the code 'temperature > 290.0' by its evaluation: 'True'. so step 2 is to evaluate the remaining code after replacement:

```python
if True:
    print("we are executing code in the if statement")
```
In the case we are asking whether 'temperature < 290.0', it replaces that block of text by False and runs the remaining code. This is a good model as to how python interprets the code.

```python
if False:
    print("we are executing code in the if statement")
```

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
`True` or `False`. You can try running the following to verify that the second line always prints: 

```python
temperature = 295.0

if temperature > 290.0:
    print("The sample is warm.")
print("This line always prints.")
```

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

## Combining Conditions

You can combine conditions with `and` and `or`.

```python
temperature = 295.0
pressure = 1.0

if temperature > 290.0 and pressure < 2.0:
    print("The experiment is in the target range.")
```

The way the `and` operator works is that both conditions must be `True`, for the overall expresssion to be evaluated as true. It works in the following way:


True and True evaluates to True
True and False evaluates to False
False and True evaluates to False
False and False evaluates to False

Question: how do you think the following evaluate:


True and True and False:
True and False and False:


How python interprets this condition: 

Python first sees: 'temperature > 290.0 and pressure < 2.0', and then evaluates 'temperature > 290.0' to True and 'pressure < 2.0' to True individually, then it has to run:

```python
if True and True:
```

for which it evaluates 'True and True' to just 'True' and evaluates the remaining code.


```python
temperature = 250.0
pressure = 5.0

if temperature < 260.0 or pressure > 4.0:
    print("Warning: check the experiment.")
```

With `or`, only one condition needs to be `True` for the expression to be 'True'.

True and True evaluates to True
True and False evaluates to True
False and True evaluates to True
False and False evaluates to False

## A Physics Example: Pulling a block in the presence of friction
Suppose you want to figure out the acceleration of a block of mass m being pulled with a string by a force F. The friction depends on whether the object is in static friction (it is not moving and a is 0) or whether it is in kinetic friction (it is moving and a is not 0). 

```python
F = 3.0
f_coeff_static = 0.4
f_coeff_kinetic = 0.3
mass = 2.0
g = 9.81

Normal_force = mass*g
max_static_friction = Normal_force*f_coeff_static

if F > max_static_friction:
    f = f_coeff_kinetic*Normal_force
    a = (F - f)/mass
else:
    f = F
    a=0

print("the acceleration is", a)
print("the friction on the block is", f)
```
Try out what happens when you pick any force greater than 7.848 Newtons (at this force, the block just starts to overcome static friction and move).
What is the smallest non-zero acceleration you can find? (we are not looking for a right answer, just play around with it for a couple of minutes)

Does your answer shed any light on why whenever you are dragging furniture it goes from still to a discontinous movement?

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

## Challenge

Write a program that finds the height of a vertically thrown projectile at a given time. Note that after it touches the ground, it does not bounce but sticks on the ground.

Use this starting point:

```python
y0 = 5.0
v0 = 8.0
g = 9.8
t = 1.0
```
and remember the equation:
y = y0 + v0 * t - 0.5 * g * t**2


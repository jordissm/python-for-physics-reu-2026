# Debugging

In this section, you will practice debugging.

Debugging means finding and fixing problems in code. Every programmer debugs.
Errors are not a sign that you are bad at programming; they are part of the
process.

The goal is to learn how to slow down, read the clues, and test one thing at a
time.

## Create a New Python File

1. Create a new file named `debugging.py`.
2. Make sure your virtual environment is active. Your terminal prompt should
   include `(reu2026_env)`.
3. Run the file from the terminal with:

   ```bash
   python3 debugging.py
   ```

At first, nothing will happen because the file is empty.

## Read Error Messages From the Bottom Up

Add this code to `debugging.py`:

```python
mass = 2.0
speed = 3.0

kinetic_energy = 0.5 * mas * speed**2

print(kinetic_energy)
```

Run the file:

```bash
python3 debugging.py
```

Python should show an error. The most useful line is usually near the bottom:

```text
NameError: name 'mas' is not defined
```

This means Python found a name it does not recognize. In this case, `mas` should
be `mass`.

Fix the typo and run the file again.

## Common Error Types

### `NameError`

A `NameError` usually means a variable or function name is misspelled or has not
been created yet.

```python
temperature = 295.0

print(tempreature)
```

Fix:

```python
temperature = 295.0

print(temperature)
```

### `SyntaxError`

A `SyntaxError` means Python cannot understand the structure of the code.

```python
if temperature > 290.0
    print("warm")
```

The problem is the missing colon.

Fix:

```python
if temperature > 290.0:
    print("warm")
```

### `IndentationError`

An `IndentationError` means the spacing at the beginning of a line is not what
Python expects.

```python
if temperature > 290.0:
print("warm")
```

Fix:

```python
if temperature > 290.0:
    print("warm")
```

### `TypeError`

A `TypeError` often means Python was given the wrong kind of value.

```python
mass = "2.0"
speed = 3.0

kinetic_energy = 0.5 * mass * speed**2
```

Here, `mass` is a string, not a number.

Fix:

```python
mass = float("2.0")
speed = 3.0

kinetic_energy = 0.5 * mass * speed**2
```

### `IndexError`

An `IndexError` often means you tried to access a list element that does not
exist.

```python
values = [10, 20, 30]

print(values[3])
```

The valid indexes are `0`, `1`, and `2`.

Fix:

```python
values = [10, 20, 30]

print(values[2])
```

## Use `print` to Inspect Values

One simple debugging tool is `print`.

```python
times = [0.0, 1.0, 2.0, 3.0]
positions = [0.0, 2.0, 4.5, 7.5]

average_speed = (positions[-1] - positions[0]) / (times[-1] - times[0])

print("times =", times)
print("positions =", positions)
print("average_speed =", average_speed)
```

Printing intermediate values helps you check whether the program is doing what
you think it is doing.

## Debug One Change at a Time

When something breaks, avoid changing five things at once. Try this pattern:

1. Read the error message.
2. Find the line number mentioned in the error.
3. Check names, punctuation, and indentation.
4. Add `print` statements if the code runs but gives the wrong answer.
5. Run the program again.

Small changes make it easier to tell what helped.

## A Physics Bug: Wrong Formula

Some bugs do not produce error messages. The program runs, but the answer is
wrong.

```python
mass = 2.0
speed = 3.0

kinetic_energy = 0.5 * mass * speed

print("kinetic energy =", kinetic_energy)
```

Python will run this code, but the formula is wrong. Kinetic energy needs
`speed**2`.

Fix:

```python
mass = 2.0
speed = 3.0

kinetic_energy = 0.5 * mass * speed**2

print("kinetic energy =", kinetic_energy)
```

Programming errors can be Python errors or physics errors. Check both.

## Use Known Answers

A good debugging habit is to test code with values where you already know the
answer.

For example:

```python
def kinetic_energy(mass, speed):
    return 0.5 * mass * speed**2

print(kinetic_energy(2.0, 3.0))
```

You can calculate this by hand:

```text
0.5 * 2.0 * 3.0**2 = 9.0
```

If Python prints `9.0`, the function passes this simple check.

## Comment Out Code Temporarily

If a file has many lines, you can temporarily comment out part of it.

```python
# print("This line will not run.")
print("This line will run.")
```

This can help you isolate the part of the program causing trouble.

Do not leave large blocks of unused code commented out forever. Once you solve
the problem, clean up the file.

## Common Beginner Mistakes

### Ignoring the line number

Error messages often include a line number. Start there, but also check the line
just above it. Missing colons or parentheses can confuse Python about where the
problem begins.

### Assuming the computer is wrong

The computer is usually doing exactly what the code says. The hard part is that
the code may not say what you meant.

### Changing too much at once

If you change many things and the program starts working, you may not know which
change fixed it. If you change many things and it breaks more, you may not know
which change caused the new problem.

## Practice

For each broken example, copy it into `debugging.py`, run it, read the error,
and fix it.

### Example 1

```python
mass = 2.0
acceleration = 9.8

force = mass * aceleraton

print(force)
```

### Example 2

```python
temperature = 295.0

if temperature > 290.0
    print("warm")
```

### Example 3

```python
values = [1.0, 2.0, 3.0]

print(values[3])
```

### Example 4

```python
radius = "2.0"
area = 3.14159 * radius**2

print(area)
```

## Challenge

This program has more than one problem. Copy it into `debugging.py`, run it,
and fix the issues one at a time.

```python
def average_speed(start_position, end_position, start_time, end_time)
    speed = end_position - start_position / end_time - start_time
    return speed

result = average_speed(0.0, 10.0, 0.0, 2.0)

print("average speed =", results)
```

The correct answer should be:

```text
average speed = 5.0
```

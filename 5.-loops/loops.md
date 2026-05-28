# Loops

In this section, you will learn how to make one set of code repeat until a condition is met.

Loops are useful when you want to do the same kind of work many times, such as:

- printing every value in a list
- computing a result for every measurement
- repeating a calculation for many times
- building up a new list of results
- many more creative uses

The two main loop commands in Python are `for` loops and `while` loops.

## Create a New Python File

1. Create a new file named `loops.py`.

## While Loop

while loops repeat a code until a 'condition' is met.

They take the following form: 
```python
x=0
while x < 5:
    print("checked that x is indeed less than 5")
    x = x + 1 #this line increases the value of x by one everytime it runs
    print("x is now:", x)
print('x is not less than 5, finish the loop and carry the proceeding code')
```
You will get the following output:
```text
checked that x is indeed less than 5
x is now: 1
checked that x is indeed less than 5
x is now: 2
checked that x is indeed less than 5
x is now: 3
checked that x is indeed less than 5
x is now: 4
checked that x is indeed less than 5
x is now: 5
x is not less than 5, finish the loop and carry the proceeding code
```
The workflow is that when python reads the while loop line, it repeats the code in the following indentation. That is, whenever it reaches the end of the block of indented code, it checks if the condition is still true, and then reruns the whole code if the condition is 'True'.

Here is question, why did it print out 'x is now: 5'. Should it not exit the code block once x hits 5?

Turns out it does not keep checking the condition constantly. It only checks it right before repeating the block of code. So it has no trouble changing the value to 5, and carrying the rest of the block. But when the block of indented code ends, it does a check of the value of x, before deciding whether to repeat the block of code.

## infinite loop 

Be careful! you could use a while condition that will never be met! The following code will be run forever because the condition to exit the while loop is never met. Note we have modified the above code to increment x by 2 each time, and the condition is to run as long as x is not equal to 5:

```python
x=0
while x != 5:
    print("checked that x is indeed not equal to 5")
    x = x + 2 #this line increases the value of x by two everytime it runs
    print("x is now:", x)
print('x is equal to 5, finish the loop and carry the proceeding code')
```
Your output will keep on going, the numbers will keep on printing.
There is no need to panic, your laptop is just exercising its gears. Click on the terminal and Press 'ctrl+c' or 'Cmd+c'(for mac) and it will end the code from running. You can always exit running code by pressing 'ctrl+c'. It is also helpful when your code is taking way too long and you do not want to wait.

## for loops

for loops are another kind of loop that helps run a code for different values of a variable. Its syntax follows 'for [Varname] in [collection]: execute code for each value in the collection. For example:

```python
for i in [0,1,2,3,4]:
    print(i)
```
This prints:

```text
1
2
3
4
5
```
The 'i' is arbitrary, it could have been 'x' or 'j' or 'ind'. Python takes this variable name and stores the current value of the list into it. For example at its first pass, python stores the value i=1, and then in the second pass it runs i=2 and so on. 
Another short hand way to do the same is to write 'for i in range(5)'. Here range is a function that creates something very similar to a list with values from 0 to 4. This is super useful if you want to run the for large lists such as from 0 to 1000.

## Example 
 For example lets calculate the Pressure of an ideal gas for different Temperatures, but with fixed volume and number of moles.

```python
temperatures = [290.0, 292.5, 295.0, 291.5]
V= 25.5
number_of_moles = 3.0
R = 8.314
calculated_pressures = [] #this is the empty list, we will append values to this.

for x in temperatures:
    print("Temperature is: ", x)
    p = number_of_moles*R*x/V
    print("Pressure is", p)
    calculated_pressures.append(p)
print("here is the list of all pressures", calculated_pressures)
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

## Challenge Question 1:
There is a old technique to calculate the equation sin(x) = x. Which is that you take sin(sin(sin(sin(sin(...sin(x)))))) enough times and hope that it reaches a natural stopping point at the solution of sin(x) = x. Because this has the property that if you take the sin(x) on both sides, it does not change the value at all. This technique can be used on a range of non-linear equations!

Challenge: Write a function that takes a value x, and takes sin(sin(sin(sin...(sin(x))))) 100 times. You can choose the starting value, x as anything you like. 

Note, the sine function is note natively defined in python for some reason, so you have to 'import' it (more on this later).

Just start your code by the following line
```python
'import numpy as np'
```

then whenever you write
```python
x=1
print(np.sin(x))
```
it will take the sine of x.

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

For the code in which we calculated pressure above, lets try changing it so that both the temperature and volume are variable. Here we do not want to use 'for x in temperature' because we also want to change volume as we go. So a solution is to loop over the numbers 0 to 3 and take the corresponding item from the list. to make sure we are taking the right number of indexes, we can use the list function len(list) to find the number of elements in temperatures. In case we add elements to the list later.

```python
temperatures = [290.0, 292.5, 295.0, 291.5]
volumes = [25.5,28.0,30.0,35.0]
number_of_moles = 3.0
R = 8.314
calculated_pressures = [] #this is the empty list, we will append values to this.

for i in range(len(temperatures)): #len calculates the number of elements in the list.
    print("Temperature is: ", temperatures[i])
    print("Volume is: ", volumes[i])
    p = number_of_moles*R*temperatures[i]/volumes[i]
    print("Pressure is", p)
    calculated_pressures.append(p)
print("here is the list of all pressures", calculated_pressures)
```

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

## Challenge 2

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

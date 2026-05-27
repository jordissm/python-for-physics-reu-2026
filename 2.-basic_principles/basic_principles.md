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
2. Run the file by clicking the 'play' button in top right of vs code screen

At first, nothing will happen because the file is empty. That is okay.

## Comments

Comments are notes for humans. Python ignores them when the program runs.

Add this to `basic_principles.py`:
```python
# This is my first basic Python practice file.
# Lines that start with # are comments.
```

Run the file again:

There should still be no output. Comments explain code, but they do not print
anything.

## Printing Values

Use `print` when you want Python to show something in the terminal.

Add this below your comments:
```python 
print("Basic principles")
print("Python is running")
```
Run the file again. You should see: the above text as output in the terminal

## Basic manipulations and Data Types

you can try doing the following operations in your python file by adding the following code:
```python
print(2*3)
print(17+4)
print(3*5*2+3)
print(2*9+(7*3))
print(True)
print(not True)
print(not not False)
print("word")
print("word1"+"word2")
```
We have to make sure that everything we write, Python understands. Python understands any number you type in directly, as well as common arithmetic operations such as '*', and '+' as it understood exactly what you meant when you wrote 2*3. it also has some in built functions it understands such as print(). We will learn some more of these in built functions soon. It also understands 'True' and 'False' mean something. 'not' can operate on 'True' and 'False'. For working with words (in coding we call these strings), we have to include quotation marks. Try running the following code without the quotations: 

```python
print(word)
```
You will notice that your terminal says 'word' is not defined. Because it tried to look up if word was defined as a built in function like 'print' or if you had specified what 'word' means somewhere (we will cover how to give meaning to 'word' in the following variables and function tutorials). 

In coding, we call text 'strings'. Notice that the '+' sign means something different for strings and numbers. Python interprets the plus symbol differently based on whether it is acting on strings or numbers. Next we will try adding a string and a number to show that it confuses python.

Whenever python does not quite understand something in your code, the terminal will print out a scary, and kind of hard to interpret descriptions of what might be wrong with the code. We will cover how to interpret these error texts later. For example here, it looked for the meaning of 'word' but could not find it and so could not run.

also try:
```python
print("word"+2)
```
You will find that it gave the following error: 
```text
TypeError: can only concatenate str (not "int") to str
```
Here str means string (for "word") and int means integer (for the number 2). The error is because it does not expect a number to be on the right of the '+' sign. Because there is a string to the left side of the '+' sign, it wants to concatenate (place a second string from the end of the first, see "word1"+"word2" above) two strings. However it gets a number and does not know how to combine the two. Notice the error message says its a 'TypeError' because you are trying to add 2 different types together. You can find the 'type' of any value by using the built in 'type()' command.

Try:
```python
print("type of 'word'", type("word"))
print("type of 1", type(1))
print("type of 1.0", type(1.0))
print("type of False", type(False))
print("type of print",type(print))
```
Note, the reason we have the comma between our string and our type command will be apparent later, its just a way to print two things with 1 command. Instead of typing print("word type)" and then print (type(word)) 

You will see that 1.0 has a different type than 1. 1.0 is a float, which means a number with decimal points. In python you can multiply floats with integers, as it just converts the integer to the corresponding decimal (1 to 1.0), but it is more efficient to store integers than decimals if you know that it can only take integer values (such as a variable that counts something). 
True and False are of the type 'Boolean' named after George Boole who worked a lot with wwhat algebra you can do with True and False values.
print is of type builtin_function since it is a native function in python. (as opposed to functions that we will write)


To make 'word'+2 work, you can tell Python to interpret the 2 as a string and so concatenate the two.

Try:
```python
print("word"+"2")
```

Exercise:
Try adding/multiplying different data types to explore which work and which don't. For example turns out multiplying a string with a integer gives a valid output, try it out! Write down the result of at least 3 such combinations. 


## Variables

We can store the values we were playing with earlier into a variable. by using the syntax of 'variable_name = *value*', we declare that whenever we type variable_name in our code, python understands it needs to retrieve the value we have assigned to it. You can re-assign new values into the same variable name too.

Add this code:
```python
time = 3.0
velocity = 12.0
distance = velocity * time

print("distance = ", distance)
```

Run the file. Python should print:

```text
36.0
```
Note: Capitalization matters for variable names. 'Time' and 'time' are different variables.

Python does the arithmetic using the values stored in the variables.

Python runs code a line at a time. So you must assign the value of a variable (with a command like variable_name = *value*) before you use it. For example try running the following code:

```python
distance = 2.0
speed = distance/time 
time = 13.5
print(speed)
```
It looks for the variable  time and since it has not been defined to python yet it throws an error.  

## Check condition

You can use '>'  signs to check if a value is greater than another
   temperature = 30
   is_higher_than_room_temperature = temperature > 25

   print(is_higher_than_room_temperature)

The expression `temperature > 25` is 'True' if temperature is greater than 25 and 'False' if it is not.

Try changing `temperature` to `20` and run the file again.

Similarly you can use '==' to check if two values are equal, and '<' to see if a value is less than another. 

## Common Beginner Mistakes

Copy the the following code and run it. You will notice that it says there is an error in the code. Find the error, and correct it.

   mass = 1.0
   acceleration = 2.0

   Print("Force = ", Mass*acceleration)   

The python 'interpreter' tries to interpret the text you have written and finds an error. In this case it can spot the error easily

# Chapter 07 — Loops

## Why Loops?

Sometimes we want to repeat a set of statements in our program — for 
instance, printing 1 to 1000. Loops make it easy to tell the computer 
which set of instructions to repeat, and how many times.

## Types of Loops in Python

There are primarily two types of loops in Python:

- `while` loops
- `for` loops

---

## While Loop

```python
while condition:   # the block keeps executing until the condition is False
    # body of the loop
```

In a `while` loop, the condition is checked **first**. If it evaluates 
to `True`, the body executes; otherwise, it doesn't. If the loop is 
entered, the process of "check condition, then execute" repeats until 
the condition becomes `False`.

**Quick Quiz:** Write a program to print 1 to 50 using a `while` loop.

### Example

```python
i = 0

while i < 5:   # prints "Nikhil" 5 times!
    print("Nikhil")
    i = i + 1
```

**Note:** if the condition never becomes `False`, the loop keeps 
executing forever (an infinite loop).

**Quick Quiz:** Write a program to print the contents of a list using a 
`while` loop.

---

## For Loop

A `for` loop is used to iterate through a sequence like a list, tuple, 
or string (these are called **iterables**).

```python
l = [1, 7, 8]

for item in l:
    print(item)   # prints 1, 7, and 8
```

### The `range()` Function

`range()` is used to generate a sequence of numbers. You can specify the 
start, stop, and step size:

```python
range(start, stop, step_size)
```

```python
for i in range(0, 7):   # range(7) also works
    print(i)   # prints 0 to 6
```

### For Loop with `else`

An optional `else` can be used with a `for` loop — it runs once the loop 
finishes normally (without a `break`).

```python
l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")   # printed once the loop finishes without breaking
```

---

## The `break` Statement

`break` exits the loop immediately when encountered.

```python
for i in range(0, 80):
    print(i)   # prints 0, 1, 2, and 3

    if i == 3:
        break
```

## The `continue` Statement

`continue` skips the rest of the current iteration and moves on to the 
next one.

```python
for i in range(4):
    print("printing")

    if i == 2:   # if i is 2, the rest of this iteration is skipped
        continue

    print(i)
```

## The `pass` Statement

`pass` is a null statement in Python — it instructs the program to "do 
nothing."

```python
l = [1, 7, 8]

for item in l:
    pass   # without pass, an empty loop body would throw an error
```

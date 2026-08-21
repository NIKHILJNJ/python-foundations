# Functions & Recursion

## What is a function?

A **function** is a group of statements that perform a specific task.

As a program grows bigger and more complex, it becomes difficult to keep 
track of which piece of code is doing what. Functions solve this by letting 
you package logic into a named, reusable block.

A function can be **reused** by the programmer any number of times, in any 
number of places, without rewriting the same logic over and over.

---

## Syntax of a function

```python
def func1():
    print('Hello')
```

This function can be called any number of times, anywhere in the program.

---

## Function Call vs Function Definition

**Function Definition** — the block containing the exact set of instructions 
that run whenever the function is called.

```python
def func1():
    print('Hello')
```

**Function Call** — whenever you want to actually run a function, you write 
its name followed by parentheses:

```python
func1()   # This is a function call
```

---

## Types of Functions in Python

There are two types of functions in Python:

1. **Built-in functions** — already provided by Python (e.g. `len()`, 
   `print()`, `range()`, `input()`).
2. **User-defined functions** — functions written by the programmer 
   (e.g. `func1()` above).

---

## Functions with Arguments

A function can accept values to work with. These values, called 
**arguments**, are placed inside the parentheses. A function can also 
**return** a value using the `return` keyword.

```python
def greet(name):
    gr = "Hello, " + name
    return gr

a = greet("Nikhil")
# a now contains "Hello, Nikhil"
```

---

## Default Parameter Values

A function parameter can be given a **default value**. If no argument is 
passed when the function is called, the default value is used instead.

```python
def greet(name="stranger"):
    print("Hello, " + name)

greet()          # name = "stranger" (default used, no argument passed)
greet("Nikhil")  # name = "Nikhil" (passed value overrides the default)
```

---

## Recursion

**Recursion** is when a function calls itself. It's often used to directly 
translate a mathematical formula into code.

### Example — Factorial

Mathematically:
```
factorial(n) = n × factorial(n-1)
```

In Python:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

### How this works

Calling `factorial(4)` triggers a chain of calls, each one waiting on the 
next, until the **base case** (`n == 0` or `n == 1`) is reached:

```
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1                  <- base case, stops the recursion

Then it unwinds:
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

Every recursive function needs two essential parts:

1. **Base case** — a condition that stops the function from calling itself 
   further (e.g. `n == 0 or n == 1`).
2. **Recursive case** — the function calling itself with a value that moves 
   closer to the base case (e.g. `n - 1`).

### A word of caution

The programmer needs to be extremely careful while working with recursion 
to ensure the function doesn't keep calling itself infinitely. A missing or 
incorrect base case will cause a `RecursionError: maximum recursion depth 
exceeded`, since Python will keep calling the function until it runs out of 
memory for new function calls.

Recursion is sometimes the most direct and natural way to express an 
algorithm — especially ones already defined mathematically in terms of 
themselves (like factorial, Fibonacci, or tree structures) — but an 
equivalent loop-based (iterative) solution can usually achieve the same 
result too.

---

## Quick Quiz

Write a program to greet a user with "Good day" using functions.

```python
def greet(name):
    print("Good day,", name)

user_name = input("Enter your name: ")
greet(user_name)
```

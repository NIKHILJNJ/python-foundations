# Chapter 02 — Variables and Datatypes

## Variables

A **variable** is the name given to a memory location in a program.

```python
a = 30        # variables = container to store a value
b = "Nikhil"  # keywords = reserved words in Python
c = 71.22     # identifiers = class/function/variable name
```

## Data Types

Primarily, Python has the following data types:

1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. `None`

Python is a fantastic language that **automatically identifies the type 
of data** for us — you never need to declare a variable's type manually.

```python
a = 71           # identified as class <int>
b = 88.44        # identified as class <float>
name = "Nikhil"  # identified as class <str>
```

## Rules for Choosing an Identifier

- A variable name can contain letters, digits, and underscores.
- A variable name can only *start* with a letter or an underscore.
- A variable name **cannot** start with a digit.
- No whitespace is allowed inside a variable name.

Examples of valid variable names: `nikhil`, `one8`, `seven_`, `_seven`.

---

## Operators in Python

1. **Arithmetic operators**: `+`, `-`, `*`, `/`, etc.
2. **Assignment operators**: `=`, `+=`, `-=`, etc.
3. **Comparison operators**: `==`, `>`, `>=`, `<`, `!=`, etc.
4. **Logical operators**: `and`, `or`, `not`.

---

## `type()` Function and Typecasting

`type()` is used to find the data type of a given variable.

```python
a = 31
type(a)   # <class 'int'>

b = "31"
type(b)   # <class 'str'>
```

A value can be converted from one type into another (if possible), using 
functions like:

```python
str(31)      # integer to string conversion
int("32")    # string to integer conversion
float(32)    # integer to float conversion
```

Here, `"31"` is a **string literal**, and `31` is a **numeric literal**.

## `input()` Function

`input()` allows the user to type in a value from the keyboard.

```python
a = input("Enter name: ")   # if the user types "Nikhil", a = "Nikhil"
```

**Important:** the output of `input()` is always a **string**, even if 
the user types a number — you must explicitly convert it with `int()` or 
`float()` if you need to use it as a number.

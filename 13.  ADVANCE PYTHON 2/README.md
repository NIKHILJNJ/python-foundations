# Chapter 13 — Advanced Python 2

## Virtual Environment

A **virtual environment** is an environment identical to the system 
Python interpreter, but isolated from other Python environments on the 
system — so packages installed in one project don't affect another.

### Installation

```bash
pip install virtualenv
```

Create a new environment:

```bash
virtualenv myprojectenv
```

After creating a virtual environment, the next step is to **activate** 
it. Once activated, it can be used just like a separate Python 
installation.

### `pip freeze` Command

`pip freeze` lists all the packages installed in a given Python 
environment, along with their versions.

```bash
pip freeze > requirements.txt
```

This creates a file named `requirements.txt` containing the output of 
`pip freeze`. You can share this file with other users, who can then 
recreate the exact same environment using:

```bash
pip install -r requirements.txt
```

---

## Lambda Functions

A **lambda function** is a function created using a single expression, 
via the `lambda` keyword.

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x
square(6)   # 36

sum_three = lambda a, b, c: a + b + c
sum_three(1, 2, 3)   # 6
```

---

## `join()` Method (Strings)

Creates a string from an iterable of strings.

```python
l = ["apple", "mango", "banana"]

result = ", and ".join(l)

print(result)   # "apple, and mango, and banana"
```

## `format()` Method (Strings)

Formats values into a string template.

```python
template.format(p1, p2, ...)
```

```python
"{} is a good {}".format("Nikhil", "student")

"{1} is a good {0}".format("Nikhil", "student")   # positions can be reordered
```

---

## Map, Filter & Reduce

**`map()`** applies a function to every item in a list.

```python
map(function, input_list)
```

**`filter()`** creates a list of items for which the function returns 
`True`.

```python
list(filter(function, input_list))
```

**`reduce()`** applies a rolling computation to sequential pairs of 
elements — collapsing a list down to a single value.

```python
from functools import reduce

val = reduce(function, list1)
```

### Example — `reduce()` computing a sum

If the function computes the sum of two numbers, and the list is 
`[1, 2, 3, 4]`, `reduce()` processes it like this:

```
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10

Final result: 10
```

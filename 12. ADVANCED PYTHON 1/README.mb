# Chapter 12 — Advanced Python 1

Following are some newly added features in the Python programming 
language.

## Walrus Operator

The walrus operator (`:=`), introduced in Python 3.8, allows you to 
assign a value to a variable **as part of an expression**.

```python
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
```

Here, `n` is assigned the value of `len([1, 2, 3, 4, 5])` and then used 
immediately in the comparison, all within the same `if` line.

## Type Hints

Type hints are added using a colon (`:`) for variables, and `->` for 
function return types.

```python
# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Usage
print(greeting("Alice"))
```

### Advanced Type Hints

Python's `typing` module provides more advanced type hints, such as 
`List`, `Tuple`, `Dict`, and `Union`.

```python
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type — value can be more than one type
identifier: Union[int, str] = "ID123"
```

---

## Match Case

Python 3.10 introduced the `match` statement — similar to the `switch` 
statement found in other programming languages.

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(200))
print(http_status(404))
```

## Dictionary Merge & Update Operators

The `|` and `|=` operators allow for merging and updating dictionaries.

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)   # {'a': 1, 'b': 3, 'c': 4}
```

Python also allows opening multiple files at once using parentheses in a 
`with` statement:

```python
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    # process files
    pass
```

---

## Exception Handling

Python raises many built-in exceptions when something goes wrong.

```python
try:
    # code which might throw an exception
    print(10 / 0)
except Exception as e:
    print(e)
```

You can catch specific exception types individually:

```python
try:
    # code
    pass
except ZeroDivisionError:
    # code
    pass
except TypeError:
    # code
    pass
except:
    # all other exceptions
    pass
```

### Raising Exceptions

You can raise your own exceptions using the `raise` keyword.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

### `try` with `else`

```python
try:
    # some code
    pass
except:
    # some code
    pass
else:
    # executed only if the try block was successful
    pass
```

### `try` with `finally`

```python
try:
    # some code
    pass
except:
    # some code
    pass
finally:
    # executed regardless of whether an error occurred
    pass
```

---

## `if __name__ == '__main__'`

`__name__` evaluates to the name of the module from where the program is 
run. If the module is being run directly from the command line, 
`__name__` is set to the string `"__main__"`.

This behavior is used to check whether a module is being run directly, 
or imported into another file.

```python
if __name__ == "__main__":
    print("Running directly")
```

## The `global` Keyword

`global` is used to modify a variable outside the current (local) scope.

```python
x = 10

def change():
    global x
    x = 20
```

## `enumerate()` Function

`enumerate()` adds a counter to an iterable and returns it.

```python
list1 = ["Nikhil", "Rohan", "Shubham"]

for i, item in enumerate(list1):
    print(i, item)
```

## List Comprehensions

A list comprehension is an elegant way to create a list based on an 
existing list.

```python
list1 = [1, 7, 12, 11, 22]

list2 = [item for item in list1 if item > 8]
```

# Chapter 09 — File I/O

## Why Files?

Random-access memory (RAM) is volatile — all its contents are lost once 
a program terminates. In order to persist data permanently, we use 
**files**.

A file is data stored on a storage device. A Python program can talk to 
a file by reading content from it and writing content to it.

## Types of Files

There are 2 types of files:

1. **Text files** (`.txt`, `.c`, etc.)
2. **Binary files** (`.jpg`, `.dat`, etc.)

Python has many built-in functions for reading, updating, and deleting 
files.

---

## Opening a File

Python's `open()` function is used to open files. It takes 2 parameters: 
the filename and the mode.

```python
# open("filename", "mode")
open("this.txt", "r")   # "r" (read) is the default mode
```

## Reading a File

```python
# Open the file in read mode
f = open("this.txt", "r")

# Read its contents
text = f.read()

# Print its contents
print(text)

# Close the file
f.close()
```

### Other Ways to Read a File

```python
f.readline()   # reads one line from the file at a time
```

## Modes of Opening a File

| Mode | Meaning |
|---|---|
| `r` | open for reading |
| `w` | open for writing |
| `a` | open for appending |
| `+` | open for updating |
| `rb` | open for reading in binary mode |
| `rt` | open for reading in text mode |

---

## Writing to a File

To write to a file, first open it in write or append mode, then use 
`f.write()`.

```python
# Open the file in write mode
f = open("this.txt", "w")

# Write a string to the file
f.write("this is nice")

# Close the file
f.close()
```

## The `with` Statement

The best way to open and automatically close a file is the `with` 
statement — it takes care of closing the file for you, even if an error 
occurs while working with it.

```python
# Open the file in read mode using 'with'
with open("this.txt", "r") as f:
    # Read the contents of the file
    text = f.read()

# Print the contents
print(text)
```

# Chapter 03 — Strings

## What is a String?

A **string** is a data type representing a sequence of characters 
enclosed in quotes. Python allows three ways to write a string:

```python
a = 'Nikhil'      # Single-quoted string
b = "Nikhil"      # Double-quoted string
c = '''Nikhil'''  # Triple-quoted string
```

## String Slicing

A string can be **sliced** to get a part of it. String indexing in 
Python starts from `0` up to `length - 1`.

```python
string[start:stop:step]
```

### Slicing with a Skip Value

```python
word = "amazing"

word[1:6:2]   # 'mzn'
```

### Other Slicing Techniques

```python
word = "amazing"

word[-7:-1]   # 'amazin'
word[:7]      # 'amazing'
word[0:]      # 'amazing'
```

---

## String Functions

1. **`len()`** — returns the length of the string.
```python
s = "Nikhil"
print(len(s))   # Output: 6
```

2. **`endswith()`** — checks if a string ends with given text.
```python
s = "Nikhil"
print(s.endswith("hil"))   # Output: True
```

3. **`count()`** — counts total occurrences of a character.
```python
s = "Nikhil"
count = s.count("i")
print(count)   # Output: 2
```

4. **`capitalize()`** — capitalizes the first character (and lowercases 
   the rest).
```python
s = "nikhil"
capitalized = s.capitalize()
print(capitalized)   # Output: Nikhil
```

5. **`find()`** — returns the index of the first occurrence.
```python
s = "Nikhil"
index = s.find("kh")
print(index)   # Output: 2
```

6. **`replace(old, new)`** — replaces the old text with the new text.
```python
s = "Nikhil"
replaced = s.replace("i", "e")
print(replaced)   # Output: Nekhel
```

---

## Escape Sequence Characters

A sequence of characters after a backslash `\` is called an **escape 
sequence** character. These represent one special character inside a 
string.

| Escape Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

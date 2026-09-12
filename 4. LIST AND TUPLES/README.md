# Chapter 04 — Lists and Tuples

## Lists

Python **lists** are containers used to store a set of values of any 
data type — including a mix of different types in the same list.

### List Indexing

A list can be indexed just like a string:

```python
l1 = [7, 9, "Nikhil"]

l1[0]   # 7
l1[1]   # 9
l1[2]   # "Nikhil"

l1[0:2]   # [7, 9]   -> list slicing
```

### List Methods

```python
l1 = [1, 8, 7, 2, 21, 15]
```

- `l1.sort()` — updates the list to `[1, 2, 7, 8, 15, 21]`
- `l1.reverse()` — updates the list to `[15, 21, 2, 7, 8, 1]`
- `l1.append(8)` — adds `8` at the end of the list
- `l1.insert(3, 8)` — adds `8` at index `3`
- `l1.pop(2)` — deletes the element at index `2` and returns its value
- `l1.remove(21)` — removes `21` from the list

---

## Tuples

A **tuple** is an immutable data type in Python — once created, it 
cannot be changed.

```python
a = ()          # empty tuple
a = (1,)        # tuple with only one element needs a trailing comma
a = (1, 7, 2)   # tuple with more than one element
```

### Tuple Methods

```python
a = (1, 7, 2)
```

- `a.count(1)` — returns the number of times `1` occurs in `a`
- `a.index(1)` — returns the index of the first occurrence of `1` in `a`

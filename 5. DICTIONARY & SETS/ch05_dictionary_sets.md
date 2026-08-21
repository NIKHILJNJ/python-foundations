# Chapter 05 — Dictionary & Sets

## Dictionary

A **dictionary** is a collection of key-value pairs.

```python
a = {
    "key": "value",
    "nikhil": "code",
    "marks": "100",
    "list": [1, 2, 9]
}

print(a["key"])    # Output: "value"
print(a["list"])   # Output: [1, 2, 9]
```

### Properties of Python Dictionaries

- It is unordered.
- It is mutable.
- It is indexed (by key, not by position).
- Cannot contain duplicate keys.

### Dictionary Methods

```python
a = {"name": "Nikhil", "from": "India", "marks": [92, 98, 96]}
```

- `a.items()` — returns a list of `(key, value)` tuples
- `a.keys()` — returns a list containing the dictionary's keys
- `a.update({"friends": ...})` — updates the dictionary with the supplied key-value pairs
- `a.get("name")` — returns the value for the specified key (safely, without crashing if the key doesn't exist)

More methods are available at docs.python.org.

---

## Sets

A **set** is a collection of non-repetitive (unique) elements.

```python
s = set()   # no repetition allowed!

s.add(1)
s.add(2)   # or: s = {1, 2}
```

If you're a programming beginner without much knowledge of mathematical 
set operations, you can simply think of sets as a data type that only 
holds unique values.

### Properties of Sets

- Sets are **unordered** — element order doesn't matter.
- Sets are **unindexed** — you cannot access elements by index.
- There is no way to change individual items in a set (though you can 
  add/remove elements).
- Sets **cannot contain duplicate** values.

### Operations on Sets

```python
s = {1, 8, 2, 3}
```

- `len(s)` — returns `4`, the length of the set
- `s.remove(8)` — updates `s`, removing `8`
- `s.pop()` — removes an arbitrary element from the set and returns it
- `s.clear()` — empties the set
- `s.union({8, 11})` — returns a new set with all items from both sets
- `s.intersection({8, 11})` — returns a set containing only the items present in both sets (here, `{8}`)

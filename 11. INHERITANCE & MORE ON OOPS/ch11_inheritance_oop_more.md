# Chapter 11 — Inheritance & More on OOP

## Inheritance

**Inheritance** is a way of creating a new class from an existing class.

```python
class Employee:   # Base class
    # code
    pass


class Programmer(Employee):   # Derived (child) class
    # code
    pass
```

We can use the methods and attributes of `Employee` in a `Programmer` 
object. We can also overwrite or add new attributes and methods in the 
`Programmer` class.

## Types of Inheritance

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance

### Single Inheritance

Occurs when a child class inherits from only a single parent class.

```
Base
  |
Derived
```

### Multiple Inheritance

Occurs when a child class inherits from more than one parent class.

```
Parent 1     Parent 2
      \       /
        Child
```

### Multilevel Inheritance

Occurs when a child class itself becomes a parent for another child 
class.

```
Parent
  |
Child1
  |
Child2
```

---

## The `super()` Method

`super()` is used to access the methods of a parent (super) class from 
within the derived class.

```python
super().__init__()   # calls the constructor of the base class
```

## Class Methods

A **class method** is a method bound to the class, not to any particular 
object of the class. The `@classmethod` decorator is used to create one.

```python
@classmethod
def some_method(cls, p1, p2):
    # code
    pass
```

---

## `@property` Decorators

```python
class Employee:
    @property
    def name(self):
        return self.ename
```

If `e = Employee()` is an object of class `Employee`, we can call 
`print(e.name)` to print `ename` — internally, this calls the `name()` 
method automatically.

## Getters and Setters

The method with the `@property` decorator is called a **getter** 
method.

We can define a matching **setter** using `@name.setter`:

```python
@name.setter
def name(self, value):
    self.ename = value
```

---

## Operator Overloading in Python

Operators in Python can be overloaded using dunder (magic) methods. 
These methods are automatically called when a given operator is used on 
objects of your class.

| Operator | Calls |
|---|---|
| `p1 + p2` | `p1.__add__(p2)` |
| `p1 - p2` | `p1.__sub__(p2)` |
| `p1 * p2` | `p1.__mul__(p2)` |
| `p1 / p2` | `p1.__truediv__(p2)` |
| `p1 // p2` | `p1.__floordiv__(p2)` |

## Other Dunder / Magic Methods

- `__str__()` — controls what gets displayed when `str(obj)` (or 
  `print(obj)`) is called.
- `__len__()` — controls what gets returned when `len(obj)` is called.

# Object Oriented Programming (OOP)

Solving a problem by creating **objects** is one of the most popular 
approaches in programming — this is called **Object-Oriented Programming**.

This concept focuses on writing reusable code, following the **DRY 
Principle** (Don't Repeat Yourself).

---

## Class

A **class** is a blueprint for creating an object.

```python
class Employee:   # class names are written in PascalCase
    # methods & variables go here
    pass
```

---

## Object

An **object** is an instantiation of a class. When a class is defined, it's 
just a template — no memory is actually allocated for data until an object 
is created from that template.

Objects of a given class can invoke the methods available to it, without 
the user needing to know how those methods are implemented internally. 
This idea is called **abstraction** and **encapsulation**.

```python
harry = Employee()   # object instantiation
```

---

## Modeling a Problem in OOP

When designing a class-based solution, a useful trick is to map parts of 
your problem description onto OOP concepts:

| Grammar | Maps to | Example |
|---|---|---|
| Noun | Class | `Employee` |
| Adjective | Attributes | `name`, `age`, `salary` |
| Verb | Methods | `getSalary()`, `increment()` |

---

## Class Attributes

A **class attribute** belongs to the class itself, rather than to any one 
specific object. All objects of that class share the same value unless 
overridden individually.

```python
class Employee:
    company = "Google"   # class attribute — shared by all objects

harry = Employee()        # object instantiation
print(harry.company)      # "Google"

Employee.company = "YouTube"   # changes the class attribute
print(harry.company)           # "YouTube" — harry sees the updated value too
```

---

## Instance Attributes

An **instance attribute** belongs to one specific object (instance), not 
to the class as a whole.

```python
harry.name = "Nikhil"
harry.salary = "30k"   # adding instance attributes directly
```

**Note:** instance attributes take priority over class attributes during 
lookup. When you access `harry.attribute`, Python checks in this order:

1. Is the attribute present on the **object** itself?
2. If not, is it present on the **class**?

---

## The `self` Parameter

`self` refers to the specific instance (object) a method is being called 
on. It's passed automatically whenever you call a method through an 
object — you never need to supply it manually.

```python
harry.getSalary()
# this is equivalent to writing: Employee.getSalary(harry)
# 'harry' is automatically passed in as 'self'
```

The method itself is defined like this:

```python
class Employee:
    company = "Google"

    def getSalary(self):
        print("Salary is not set yet")
```

---

## Static Methods

Sometimes a method inside a class doesn't need to use `self` at all — it 
doesn't depend on any particular object's data. For these cases, you can 
define a **static method** using the `@staticmethod` decorator.

```python
class Employee:

    @staticmethod
    def greet():
        print("Hello user")
```

A static method is called on the class (or an object) without Python 
automatically passing in `self`:

```python
Employee.greet()   # "Hello user" — no object needed
```

---

## The `__init__()` Constructor

`__init__()` is a special method that runs **automatically** the moment an 
object is created. It's commonly called the **constructor**.

It always takes `self` as its first argument, and can take additional 
arguments used to set up the object's initial state.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def getSalary(self):
        print(f"{self.name}'s salary is not set yet")

nikhil = Employee("Nikhil")   # __init__ runs automatically, self.name = "Nikhil"
nikhil.getSalary()             # "Nikhil's salary is not set yet"
```

### Why `__init__()` is useful

Without a constructor, you'd have to manually set every instance attribute 
one line at a time after creating each object (as shown earlier with 
`harry.name = "Nikhil"`). `__init__()` lets you set them up in one step, 
right when the object is created — and ensures every object of that class 
starts out with the attributes it needs.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

nikhil = Employee("Nikhil", "30k")
print(nikhil.name)     # "Nikhil"
print(nikhil.salary)   # "30k"
```

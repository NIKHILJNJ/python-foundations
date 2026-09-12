# Chapter 06 — Conditional Expressions

## Why Conditionals?

Sometimes we want to play a game on our phone if the day is Sunday.
Sometimes we order ice cream online if the day is sunny.
Sometimes we go hiking if our parents allow.

All of these are decisions that depend on a condition being met. In 
Python too, we need to be able to execute instructions only when certain 
condition(s) are met — this is what **conditionals** are for.

## If, Elif, and Else

`if`, `elif`, and `else` let a program make a multi-way decision based on 
conditions in the code.

```python
if condition1:      # if condition1 is True
    print("yes")
elif condition2:    # if condition2 is True
    print("no")
else:                # otherwise
    print("maybe")
```

### Example

```python
a = 22

if a > 9:
    print("greater")
else:
    print("lesser")
```

**Quick Quiz:** Write a program to print "yes" when the age entered by 
the user is greater than or equal to 18.

---

## Relational Operators

Relational operators are used to evaluate conditions inside `if` 
statements:

- `==` — equals
- `>=` — greater than or equal to
- `<=` — less than or equal to

## Logical Operators

Logical operators combine or invert conditional statements:

- `and` — True if **both** operands are true, else False
- `or` — True if **at least one** operand is true, else False
- `not` — inverts True to False, and False to True

## The `elif` Clause

`elif` means "else if." An `if` statement can be chained together with 
multiple `elif` statements, followed by an optional `else`.

```python
if condition1:
    # code
elif condition2:      # this ladder stops once a condition is met
    # code
elif condition3:
    # code
else:
    # code
```

### Important Notes

1. There can be any number of `elif` statements.
2. The final `else` only runs if **all** the conditions in the `if`/`elif` chain fail.

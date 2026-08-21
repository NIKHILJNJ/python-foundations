# Chapter 11 — Practice Set: Inheritance & More on OOP

1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
2. Create a class 'Pets' from a class 'Animals', and further create a class 'Dog' from 'Pets'. Add a method 'bark' to the 'Dog' class.
3. Create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' with a `@property` decorator and a matching setter, which changes the value of increment based on the salary.
4. Write a class 'Complex' to represent complex numbers, along with overloaded `+` and `*` operators which add and multiply them.
5. Write a class 'Vector' representing a vector of n dimensions. Overload the `+` and `*` operators to calculate the sum and the dot (.) product of two vectors.
6. Write a `__str__()` method to print the vector as follows (assume a vector of dimension 3 for this problem):
   ```
   7i + 8j + 10k
   ```
7. Override the `__len__()` method on the vector from problem 5, to display the dimension of the vector.

## Project 2: The Perfect Guess

Write a program that generates a random number and asks the user to 
guess it.

- If the player's guess is higher than the actual number, the program 
  displays "Lower number please".
- If the user's guess is too low, the program prints "Higher number 
  please".
- When the user guesses the correct number, the program displays the 
  number of guesses the player used to arrive at the answer.

**Hint:** `import random`

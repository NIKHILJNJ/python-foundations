a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try: 
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("thank you for using the program.")    
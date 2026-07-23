num =int(input("Enter a number: "))

p = 1

for i in range (num,0,-1):
    p = p * i
print("The factorial of", num, "is", p)
num = int(input("Enter a number: "))

s = 0

if num < 0:
    print("Please enter a non-negative integer.")
else:
    for i in range(1,num +1):
        s = s + i
    print("The sum of first", num, "natural numbers is", s)

# a simpler formula for sum of first n natural numbers is n(n+1)/2    
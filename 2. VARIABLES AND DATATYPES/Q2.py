x = int(input("Enter a number (divisor): "))

y = int(input("Enter a number (dividend): "))

z = y % x # % is the modulus operator which gives the remainder of the division of y by x.

if(z == 0):
    print("The remainder is zero.")
else:
    print("The remainder is" , z)    
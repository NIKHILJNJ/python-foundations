num = int(input("Enter a small number: "))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end="")       
    print()

# end="" is used to print the stars in the same line. 
# The inner loop prints the stars and the outer loop moves to the next line after printing each row of stars.
#print() is used to move to the next line after printing each row of stars.
class calculator:
    def __init__(nj, num1):
        nj.num1 = num1
        

    def sq (nj):
        print(f"Square of {nj.num1} is: {nj.num1**2}")

    def cube (nj):
        print(f"Cube of {nj.num1} is: {nj.num1**3}")

    def sqrt (nj):
        print(f"Square root of {nj.num1} is: {nj.num1**0.5}")


a = float(input("Enter a number: "))
b = int(input("Enter 1 for square, 2 for cube, 3 for square root: "))

if b not in (1,2,3):
    print("Invalid input. Please enter 1, 2, or 3.")
else:    

    calc = calculator(a)
    if b==1:
        calc.sq()
    elif b==2:
        calc.cube()
    elif b==3:
        calc.sqrt()


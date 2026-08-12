class calculator:
    def __init__(self, num1):
        self.num1 = num1
        

    def sq (self):
        print(f"Square of {self.num1} is: {self.num1**2}")

    def cube (self):
        print(f"Cube of {self.num1} is: {self.num1**3}")

    def sqrt (self):
        print(f"Square root of {self.num1} is: {self.num1**0.5}")

    @staticmethod 
    def greet():
        print("Hello! Welcome to the calculator program.")   


a = float(input("Enter a number: "))
b = int(input("Enter 1 for square, 2 for cube, 3 for square root: "))

if b not in (1,2,3):
    print("Invalid input. Please enter 1, 2, or 3.")
else:    

    calc = calculator(a)
    if b==1:
        calc.sq()
        calc.greet()
    elif b==2:
        calc.cube()
        calc.greet()
    elif b==3:
        calc.sqrt()
        calc.greet()


                   
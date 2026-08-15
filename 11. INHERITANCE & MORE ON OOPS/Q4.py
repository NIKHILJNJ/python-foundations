class mycomplex :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):    
        return mycomplex(self.x + other.x, self.y + other.y)
    
    # __add__is a special method that is used to add two objects of the same class.
    #  It takes two parameters, self and other, where self refers to the current object and other refers to the object being added. 
    # The method returns a new object of the same class with the sum of the attributes of the two objects.
    
    def __mul__(self,other):    
            real_part = self.x * other.x - self.y * other.y
            imag_part = self.x * other.y + self.y * other.x
            return mycomplex(real_part, imag_part)
    
    def __str__(self):
        return (f"{self.x},{self.y}i")
    # __str__ is a special method that is used to return a string representation of an object.
    
           

c = int(input("enter 1 for adittion and 2 for multiplication : "))

if c == 1:
    x = int(input("Enter the 1st real part of mycomplex number : "))
    y = int(input("Enter the 1st imaginary part of mycomplex number : "))
    obj1 = mycomplex(x, y)
    x2 = int(input("Enter the 2nd real part of mycomplex number : "))
    y2 = int(input("Enter the 2nd imaginary part of mycomplex number :"))
    obj2 = mycomplex(x2, y2)
    print("The sum mycomplex numbers is:", obj1 + obj2)
elif c == 2:
    x = int(input("Enter the 1st real part of mycomplex number : "))
    y = int(input("Enter the 1st imaginary part of mycomplex number :"))
    obj3 = mycomplex(x, y)
    x2 = int(input("Enter the 2nd real part of mycomplex number : "))
    y2 = int(input("Enter the 2nd imaginary part of mycomplex number : "))
    obj4 = mycomplex(x2, y2)
    print("The product of mycomplex numbers is: ", obj3 * obj4) 
else:
    print("Invalid input")            
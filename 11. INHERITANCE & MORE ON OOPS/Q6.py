class two_d :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):    
        return two_d(self.x + other.x, self.y + other.y)
    
    # __add__is a special method that is used to add two objects of the same class.
    #  It takes two parameters, self and other, where self refers to the current object and other refers to the object being added. 
    # The method returns a new object of the same class with the sum of the attributes of the two objects.
    
    def __str__(self):
        return (f"{self.x}i + {self.y}j")
    # __str__ is a special method that is used to return a string representation of an object.
    


class three_d(two_d): 
# inheriting the properties of two_d class
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):
        return three_d(self.x + other.x, self.y + other.y, self.z + other.z) 
    def __str__(self):
            return (f"{self.x}i+ {self.y}j+ {self.z}k")
           

c = int(input("enter 2 for 2- objects and 3 for 3-d objects:"))

if c == 2:
    x = int(input("Enter the length of 1st 2-d object:"))
    y = int(input("Enter the breadth of 1st 2-d object:"))
    obj1 = two_d(x, y)
    x2 = int(input("Enter the length of 2nd 2-d object:"))
    y2 = int(input("Enter the breadth of 2nd 2-d object:"))
    obj2 = two_d(x2, y2)
    print("The sum of 2-d objects is:", obj1 + obj2)
elif c == 3:
    x = int(input("Enter the length of 3-d object:"))
    y = int(input("Enter the breadth of 3-d object:"))
    z = int(input("Enter the height of 3-d object:"))
    obj3 = three_d(x, y, z)
    x2 = int(input("Enter the length of 2nd 3-d object:"))
    y2 = int(input("Enter the breadth of 2nd 3-d object:"))
    z2 = int(input("Enter the height of 2nd 3-d object:"))
    obj4 = three_d(x2, y2, z2)
    print("The sum of 3-d objects is:", obj3 + obj4) 
else:
    print("Invalid input")            
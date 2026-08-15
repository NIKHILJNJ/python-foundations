class three_d(): 
# inheriting the properties of two_d class
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return three_d(self.x + other.x, self.y + other.y, self.z + other.z) 

 # rmenber the three_d() warapper is used because we are returning a new object of the same class with the sum of the attributes of the two objects.

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

#in the __mul__ method, we are calculating the dot product of two 3-d objects.

# it is a single value that why we are not returning a new object of the same class but a single value and wrapper is not needed.

    def __str__(self):
            return (f"{self.x},{self.y},{self.z}")
           

x = int(input("Enter the length of 3-d object:"))
y = int(input("Enter the breadth of 3-d object:"))
z = int(input("Enter the height of 3-d object:"))
obj3 = three_d(x, y, z)
x2 = int(input("Enter the length of 2nd 3-d object:"))
y2 = int(input("Enter the breadth of 2nd 3-d object:"))
z2 = int(input("Enter the height of 2nd 3-d object:"))
obj4 = three_d(x2, y2, z2)

print("The sum of 3-d objects is:", obj3 + obj4) 
print("The dot product of 3-d objects is:", obj3 * obj4) 

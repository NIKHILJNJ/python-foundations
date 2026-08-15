class animal:
    pass
class pet(animal):
    pass
class dog(pet):
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"    

name = input("Enter the name of the dog: ")
my_dog = dog(name)
print(my_dog.bark())    
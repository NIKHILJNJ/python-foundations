class Employee:
    def __init__(self ,name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def salaryafterIncrement(self):
        return self.salary + self.increment    

    @salaryafterIncrement.setter
    def salaryafterIncrement(self, value):
        self.increment = value - self.salary

name = input("Enter the name of the employee: ")

salary = int(input("Enter the salary of the employee: "))

increment = int(input("Enter the increment of the employee: "))

emp = Employee(name, salary, increment)

print(f"Salary after increment for {emp.name} is: {emp.salaryafterIncrement}")

new = int(input("Enter the new salary after increment: "))
emp.salaryafterIncrement = new
print(f"New increment for {emp.name} is: {emp.increment}")

    
class programmer:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary


add_more = "y"

programmers =[] # list can also store multiple programmer objects

while add_more == "y":
    name = input("Enter the name of the programmer: ")
    language = input("Enter the programming language: ")
    salary = float(input("Enter the salary: "))

    prog = programmer(name, language, salary) 
    programmers.append(prog) # add the programmer object to the list

    print(f"Programmer Name: {prog.name}")
    print(f"Programming Language: {prog.language}")
    print(f"Salary: {prog.salary}")

    add_more = input("Do you want to add another programmer? (y/n): ")

print("\n list of programmers: ")
for p in programmers:
    print(f"Programmer Name: {p.name}, Programming Language: {p.language}, Salary: {p.salary}")



num = int(input("Enter a number: "))

list1 = [i*num for i in range(1, 11)]

print(f"The multiplication table of {num} is:")

print(list1)

with open("table.txt", "w") as f:
    f.write(f"The multiplication table of {num} is:\n")
    f.write(str(list1))
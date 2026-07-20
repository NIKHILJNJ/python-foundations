s = set()

a = int(input("Enter the number you want to add to the set: "))

s.add(a)

b = float(input("Enter a floating point number you want to add to the set: "))
s.add(b)

c = input("Enter a string you want to add to the set: ")
s.add(c)

print("Contents of the set:", s)    

print("the length of the set is: ", len(s), "\n" , "the set can contain different data types together, as shown in the output above")
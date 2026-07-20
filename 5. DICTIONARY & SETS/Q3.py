s = set()

a = int(input("Enter the number you want to add to the set: "))

s.add(a)

t = input("Enter the number you want to add to the set: ")

s.add(t)

print("Contents of the set:", s)

print("type of the number you entered first is: ", type(a))

print("type of the number you entered second is: ", type(t) ,"\n" , "the second input was taken as a string that means that sets can contain different data types together" )

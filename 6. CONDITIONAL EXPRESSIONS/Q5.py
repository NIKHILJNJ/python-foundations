names = input("Enter list of names separated by commas: ").split(",")

names = [n.strip() for n in names]

#expended version of the code
#newlist = []
# for n in names:
# newlist.append(n.strip())
#names = newlist


name = input("Enter a name to check if it is in the list: ")

for n in names:
    if n == name:
        print("Name is in the list")
        break
else:
    print("Name is not in the list")
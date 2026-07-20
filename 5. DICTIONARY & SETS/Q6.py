s = {}

for i in range(4):

    name = input("Enter your name : ")

    lang =input("Enter your language : ") 

    s[name]=lang

print(s) 

# Note: if the same name is entered more than once, the dictionary will 
# only keep the last language entered for that name, since dict keys must be unique.
# if you want it to work with multiple languages for the smae name use if to check if the name is already in the dictionary.
# then append the new language to a list of languages for that name. 
# or just give the user a warning that the name is already in the dictionary and ask them to enter a different name.
# and inorder not to interrupt the program just use continue to skip the rest of the loop and go to the next iteration.
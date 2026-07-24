name = input("Enter the list of names: ").split(",")

name = [n.strip().capitalize() for n in name]

check = input("Enter the letter you want to check: " ).capitalize()

if len(check) != 1 :
    print("Please enter only one letter.")
   
else:
    for n in name:
        if n.startswith(check) :

            print(f"HELLOW {n}!")

        else :
            print(f"'{n}' does not start with the letter '{check}'")     
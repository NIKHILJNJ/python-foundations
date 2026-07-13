name = []
while (1>0):
        a = input("enter a name or enter stop to end the input ")
        if (a == "stop" ):
                break
        name.append(a)        

b = input("enter the neame to be checked =")
if b in name:
        print("name is present ")


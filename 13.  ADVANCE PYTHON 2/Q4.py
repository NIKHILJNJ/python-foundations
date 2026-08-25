l =[]

for i in range (10):
    l.append(int(input("enter a number for the list: ")))

div = lambda x:x%5==0


fl = filter (div,l) 

print(list(fl))

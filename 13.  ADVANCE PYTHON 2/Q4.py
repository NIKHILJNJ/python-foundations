l =[]

for i in range (10):
    l.append(int(input("enter a number for the list: ")))

def div(s):
    if s%5==0:
        return s
    else:
        return False   


fl = filter (div,l) 

print(list(fl))

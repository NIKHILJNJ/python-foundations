from functools import reduce
# reduce isn't a built-in function in Python 3. It lives in the functools module, so you need to import it first.
l =[]

for i in range (10):
    l.append(int(input("enter a number for the list: ")))

def greater(a,b):
    if(a>b):
        return a
    elif(b>a):
        return b
    else:
        return a

fl = reduce (greater,l)    

print(f"the greatest number in the list is {fl}")
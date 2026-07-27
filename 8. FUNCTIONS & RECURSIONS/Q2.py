
def temps(a,b):
    if (b==1):
        c= (a-32)*5/9
        return c
    else:
      f =(a*1.8)+32
      return f



t = float(input("Enter the temps in numerical value only : "))

s = int(input("Enter 1 for F TO C and 2 for C to F: "))

if s != 1 and s != 2:
   print("enter valid options")
else:
   print("the converted temperature is :",temps(t,s))


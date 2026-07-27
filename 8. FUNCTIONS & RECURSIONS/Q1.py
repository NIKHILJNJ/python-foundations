def greatest(a,b,c):

    if(a>b and a>c):

        return a
    
    elif(b>a and b>c):

        return b

    else:
        return c

a = int(input("enter a number: "))    
b  = int(input("enter a number: "))  
c  = int(input("enter a number: "))  

if (a==b or b==c or c==a):
    print("Please enter three different numbers")
else:    
  print("the greatest no is", greatest(a,b,c))

# well you should use  if (a==b or b==c or c==a): in function if you every want to reuse this function elsewhere
# also use float(input()) if you want to use decimal input in the program
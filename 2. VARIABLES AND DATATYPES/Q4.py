a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

if(a > b):
    print(a, "is greater than", b) 

#In python make sure to use elif instead of else if and make sure of indentation as python is indentation sensitive language.   
    
elif(a < b):    
    print(a, "is less than", b)

else:
    print(a, "is equal to", b)
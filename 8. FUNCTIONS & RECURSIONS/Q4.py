def sum_number(n) :
   if n == 0:
        return 0
   elif n == 1:
        return 1
   else:
    return n+sum(n-1)

n = int(input("enter a positive number: "))

if (n<0):
  print ("enter correct input")
else:
  print("the sum of first n natural numbers is ", sum_number(n))

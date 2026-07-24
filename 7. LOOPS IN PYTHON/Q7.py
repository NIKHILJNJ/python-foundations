num = int(input("Enter a small number: "))

e = []

f= 1

while(len(e)<= num-1):

   if (f%2==1):
      e.append(f)
   f = f+1

# f=f+2 will also work because there is 2 digit difference between odd numbers and if is not needed

# e = [2 * i + 1 for i in range(num)] is also an option

for i in range (1,num+1):
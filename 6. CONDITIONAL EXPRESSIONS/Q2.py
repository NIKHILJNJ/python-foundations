f = int(input("Enter the marks of first subject: "))

s = int(input("Enter the marks of second subject: "))

t = int(input("Enter the marks of third subject: "))

total = (f+s+t)/3

if (f>=33 and s>=33 and t>=33) and total>=40:

    print("Pass")

else:
     if f<33 or s<33 or t<33:

        print("Fail - one or more subjects below passing marks (33)")

     elif total < 40:
      
      print("Fail - overall average below 40")
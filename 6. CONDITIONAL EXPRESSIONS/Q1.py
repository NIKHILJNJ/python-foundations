a =[]

for i in range(4):
    b = int(input("Enter a number: "))
    a.append(b)

if a[0] >= a[1] and a[0] >= a[2] and a[0] >= a[3]:
    print("The largest number is:", a[0])
elif a[1] >= a[0] and a[1] >= a[2] and a[1] >= a[3]:
    print("The largest number is:", a[1])
elif a[2] >= a[0] and a[2] >= a[1] and a[2] >= a[3]:
    print("The largest number is:", a[2])
else:
    print("The largest number is:", a[3])

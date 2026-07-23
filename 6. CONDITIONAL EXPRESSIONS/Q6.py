marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("You got an EX")
elif marks >= 80 and marks < 90:
    print("You got an A")
elif marks >= 70 and marks < 80:
    print("You got a B")
elif marks >= 60 and marks < 70:
    print("You got a C")
elif marks >= 50 and marks < 60:
    print("You got a D")
else:
    print("You got an F")        
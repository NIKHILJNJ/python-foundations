a = int(input("enter numbers : "))
b = int(input("enter numbers : "))
c = int(input("enter numbers : "))

if a >= 33 and b >= 33 and c >= 33:
    if ((a+b+c)/300)*100 > 40 :
        print("PASS")
    else:
        print("FAIL IN TOTAL PERCENTAGE ")    

else:
    print("FAIL IN SUBJECT")
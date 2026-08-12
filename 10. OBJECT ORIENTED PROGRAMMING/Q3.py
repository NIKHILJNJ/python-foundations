class check:
    a = 10


change = check()
change.a = 0
if check.a == change.a:
    print("Class variable is changed")
else:
    print("Class variable is not changed")   

     
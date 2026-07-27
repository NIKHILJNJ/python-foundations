def conversion(a,b):
    if b==1:
        print(round(( a*2.54, "cm")))
        return
    else:
        print(round((a/2.54, "inches")))
        return

print("which type of conversion is needed select 1. For inches to cm  2. For cm to inches ")

# here """ """ will look better here

selection = float(input("enter the selected option : "))

digits = float(input("enter the values for converstion :"))

if selection in (1,2):
    conversion(digits,selection)
else:
    print("enter correct input")

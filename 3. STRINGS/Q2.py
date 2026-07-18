from datetime import date

# From datetime module, we are importing date class to get the current date. 
# We can also use datetime module to get the current date and time.

now = date.today()

# Getting the current date using date.today() method. It returns the current local date.
# now() instead today() method returns the current local date and time. But for that we need to import datetime class from datetime module.

name = input("Enter your name: ")

print( f"Dear {name}, \n You are selected! \n Date: {now}")
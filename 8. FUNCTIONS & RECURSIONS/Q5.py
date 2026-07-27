def pattern(n):
    if (n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)

# In recursion what is most needed is a stopping statement which in this is if(n==0): return
# also from what I observe recursion is like a decreasing version of loop 
n = int(input("enter a number :"))

pattern(n)


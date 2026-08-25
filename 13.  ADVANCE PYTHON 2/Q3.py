t  = int(input("enter a number: "))

table =[str(t*i) for i in range(1,11)]
# .join() — combining a list of strings into one string
i = "\n".join(table) 
print(i)

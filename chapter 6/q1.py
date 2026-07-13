l = []
for a in range(4):
    i = int(input ( "enter a number:" ) )
    l.append(i)
 
if ( l[1] > l[2] and l[1] >l[3] and l[1] > l [0] ):   
        print(l[1], "is the greatest")

elif ( l[2] > l[1] and l[2] >l[3] and l[2] > l [0] ):   
        
        print(l[2], "is the greatest")

elif ( l[3] > l[2] and l[3] >l[1] and l[3] > l [0] ):   
        
        print(l[3], "is the greatest")
else:
       print(l[0], "is the greatest") #just use max()
              

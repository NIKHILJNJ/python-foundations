l1 = [1,2,3,4,5,6,7]

for i, j in enumerate(l1):
    if i==2 or i==4 or i==6:
        print(j)

# index starts with 0, so the 3rd element is at index 2, the 5th element is at index 4, and the 7th element is at index 6. 
# The enumerate() function returns both the index and the value of each element in the list.        


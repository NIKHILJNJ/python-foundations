fruits = []


for i in range(0,7):

    a = input(f"enter a fruit name {i}: ")

# a[i] =  input(f"enter a fruit name {i}: ") cannot be used because it tries to assign a value into an existing list at index i — but a doesn't exist yet as a list, so Python has nothing to index into.

    fruits.append(a)

# fruits.append(a) because we are building the list from scratch (not overwriting existing positions), we want .append(), not indexed assignment

# a[i] can work if we add this line before the loop: a = [None] * 7, which creates a list of 7 None values, so that we can assign to a[i] in the loop. But this is not necessary if we just want to build a list from scratch.

print(fruits)

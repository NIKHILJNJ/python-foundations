a = input("Enter a sentence: ")

while ("  " in a):

    a = a.replace("  "," ")


# without the while loop, only the first occurrence of multiple spaces would be replaced.

print(a)

# (cleaner alternative): split on any whitespace, rejoin with single spaces
# a = " ".join(a.split())
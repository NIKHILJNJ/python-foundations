a = input("Enter a sentence: ")

if(a.count("  ") > 0) :

    print("The sentence contains multiple spaces. Also, the number of multiple spaces is: ", a.count("  "))

 # Note: count() finds non-overlapping occurrences of "  ". 
 # So 3 spaces in a row (e.g. "a   b") counts as only 1 occurrence, not 2.


else:

    print("The sentence does not contain multiple spaces.")

# Alternative approach using find():
# find() returns the index of the first occurrence, or -1 if not found.
# So checking `a.find("  ") != -1` also tells you if a double space exists.
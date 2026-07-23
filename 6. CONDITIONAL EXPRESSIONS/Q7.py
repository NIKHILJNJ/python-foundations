post = input("Enter your post: ").lower()

name = input("Enter a name to check if it is in the post: ").lower()

if name in post:
    print("This post contains the name")
else:
    print("This post does not contain the name")

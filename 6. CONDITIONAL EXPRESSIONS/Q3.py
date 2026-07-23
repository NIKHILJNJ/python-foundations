comment = input("Enter a comment: ").lower()

spam = ["make money fast", "buy now", "subscribe this", "click this"]

for phrase in spam:
    if phrase in comment:
        print("This comment is spam")
        break

# spam in comment can not be used because it will check if the entire list is in the comment, 
# which is not what we want. We want to check if any of the phrases in the list are in the comment.
# also any(phase in comment for phrase in spam) can be used to check if any of the phrases in the list are in the comment.


else:
    print("This comment is not spam")
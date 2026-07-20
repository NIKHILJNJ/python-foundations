comment = input("Enter a comment: ").lower()

spam = ["make money fast", "buy now", "subscribe this", "click this"]

if spam in comment:
    print("This comment is spam")
else:
    print("This comment is not spam")
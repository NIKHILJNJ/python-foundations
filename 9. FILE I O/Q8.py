with open("poems.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
     f.write(content)    
# w mode creats a new file if it does not exist, or truncates the file if it exists.
          
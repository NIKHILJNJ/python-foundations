with open("poems.txt") as f:
    content = f.read()

with open("copy.txt") as f:
      copy_content = f.read()

if (content == copy_content):
    print("The files are identical & matches the content.")
else:
     print("the files are not identical & matches the content.")       

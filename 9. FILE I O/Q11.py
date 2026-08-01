with open("poems.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
     f.write(content) 

# we can use os module to correctly rename the file, but here we are using file handling to rename the file by creating a new file with the same content and deleting the old file.     
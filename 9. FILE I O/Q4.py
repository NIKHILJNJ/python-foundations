
with open("A4.txt","r") as f:
    content = f.read()
    print (content)

word = input("Enter the word to mask: ")

content = content.replace(word,"#"*len(word))

with open("A4.txt","w") as f: 
    f.write(content)
    print("the content is updated : ")
    print(content)      




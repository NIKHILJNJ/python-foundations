import re
#The import re statement imports Python's built-in Regular Expression (RegEx) module. This native library lets you search, split, replace, and extract specific text configurations using specialized pattern strings

with open("A4.txt","r") as f:
    content = f.read()
    print (content)

word = input("Enter the words to mask : ").capitalize().split(",")
words = [n.strip() for n in word]

for n in words:
    content = re.sub(re.escape(n), "#" * len(n), content, flags=re.IGNORECASE)

# re.sub(pattern, replacement, text)	Replace matches with something else
# Breaking down re.sub(pattern, replacement, text, flags)
# pattern — what to search for (can be a literal word, or a complex pattern with special symbols)
# replacement — what to replace matches with
# text — the string to search within
# flags=re.IGNORECASE — an optional setting telling re to ignore uppercase/lowercase differences while matching
#re.escape(n) converts your plain word into a "safe" pattern where every character is treated literally, avoiding accidental regex syntax conflicts. This matters more once your masked words might contain punctuation

with open("A4.txt","w") as f: 
    f.write(content)
    print("the content is updated : ")
    print(content)      


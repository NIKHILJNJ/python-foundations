import re
with open("log.txt", "r") as f:
    content = f.read()
    print(content)

word = input("Enter a word to search for: ")
if re.search(word, content, re.IGNORECASE):
    print(f"The word '{word}' was found in the log.")
else:
    print(f"The word '{word}' was not found in the log.")

#    Comparing your options — in, .find(), and re.search()
#  Method	                        Case-sensitive?	                          Returns
#"donkey" in text		                Yes                                  True/False
# text.find("donkey")		            Yes                                  Index or -1
# re.search("donkey", text, flags=re.IGNORECASE)	No (ignores case)	Match object or None
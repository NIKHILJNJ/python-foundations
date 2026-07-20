HINDI = {  "Namaste": "Hello / Greetings",
"Dhanyavaad": "Thank you",
"Kripya": "Please",
"Shukriya": "Thanks",
"Pyaar": "Love",
"Dosti": "Friendship",
"Aasha": "Hope",
"Khushi": "Happiness",
"Dukkh": "Sadness",
"Shanti": "Peace",
"Jal": "Water",
"Bhojan": "Food / Meal",
"Ghar": "Home",
"Vidyalaya": "School",
"Kitaab": "Book",
"Adhyapak": "Teacher",
"Chhatra": "Student",
"Gaadi": "Vehicle / Car",
"Sagar": "Ocean",
"Pahad": "Mountain",
"Suraj": "Sun",
"Chand": "Moon",
"Taare": "Stars",
"Mausam": "Weather",
"Jeevan": "Life",
"Samay": "Time",
"Sapna": "Dream",
"Duniya": "World",
"Safar": "Journey",
"Swatantrata": "Freedom",

 }

print("Hindi words of which we can provide translation ",HINDI.keys())


a = input("enter the word you need meanning ").strip() .capitalize()  

# .strip() removes any leading or trailing whitespace from the input.
# .capitalize() capitalizes the first letter of the input.


Meaning = HINDI.get(a, "Sorry, the word is not in the dictionary")

# .get() method is used to retrieve the value associated with a key in a dictionary.
# If the key is not found, it returns the specified default value, which in this case is "Sorry, the word is not in the dictionary".

print("the meaning of", a, "is", Meaning)
# intall pyttsx3 first using pip install pyttsx3 and make sure you have espeak installed in your system. If you are using windows then you can install it using pip install pywin32

import pyttsx3 

engine = pyttsx3.init()

engine.say("Twinkle twinkle little star how I wonder what you are Up above the world so high like a diamond in the sky ")

engine.runAndWait()
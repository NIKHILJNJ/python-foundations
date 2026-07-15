# Made with AI in order to show complex programs following code with harry videos instructions for this particular question.
# Import the os module - it lets Python interact with the operating system
# (file system, directories, environment variables, etc.)
import os

# Ask the user to type a folder path
# If they just press Enter without typing anything, path will be an empty string
path = input("Enter the path of the folder (press Enter for current directory): ")

# Check if the user left the input blank
# .strip() removes any accidental spaces before checking
if path.strip() == "":
    # "." means "current directory" - wherever the terminal is currently pointing
    path = "."

# try/except is used here to handle errors gracefully instead of crashing
try:
    # os.listdir(path) returns a list of all file and folder names inside 'path'
    contents = os.listdir(path)

    # Print a header showing which folder we're listing
    print(f"\nContents of '{path}':")

    # Loop through each item in the list and print it on its own line
    for item in contents:
        print(item)

# This runs if the folder path doesn't exist at all
except FileNotFoundError:
    print("That directory doesn't exist.")

# This runs if Python doesn't have permission to read that folder
except PermissionError:
    print("You don't have permission to access that directory.")
with open("log.txt", "r") as f:
    content = f.readlines()
# readlines() method reads the entire file and returns a list of lines in the file. Each line is a string in the list.
found = False
count = 1

for line in content:
    if "python" in line:
        print(f"Python found in line {count}")
        found = True
    count += 1

if not found:
    print("Python not found in the file.")
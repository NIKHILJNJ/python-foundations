for i in range(3):
    for j in range(3):
        if (i == 1 and j == 1):
            print(" ", end="")   # print a space instead of a star
        else:
            print("*", end="")
    print()
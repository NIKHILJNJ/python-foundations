import random

def game():
    print("You are playing a game of fates: Random Number!")
    score = random.randint(1,100)

    print(f"your score is {score} out of 100")
    with open("Hi-score.txt","r") as f :
        hi = f.read()
    if(hi != ""):
        hi=int(hi)
    else:
        hi=0

    if score > hi:
        print("New High Score!")
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
#also the file name Hi-score.txt is required before running the program try and except can solve this
        

game() 


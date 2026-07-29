"""
1 is for ROCK
2 is for PAPPER
3 is for SCISSORS

"""
import random

meaning = {1:"ROCK", 2:"PAPPER" , 3:"SCISSORS"  }
play_again = "y"

while play_again == "y":
      
    computer = random.choice ([1,2,3])

    you = int(input("Enter 1 FOR ROCK , 2 FOR PAPPER , 3 FOR SCISSORS:  ")    )

    if( you not in (1,2,3)):
        print("ENTER CORRECT INPUT")

    else:
        if(computer==you):
            print( f"IT's a Draw your choice is {meaning[you]} and computer's is {meaning[computer]}")           
        elif(computer == 1 and you == 2 ):
            print(f"You win your choice is {meaning[you]} and computer's is {meaning[computer]}")                            
        elif(computer == 1 and you == 3 ):
            print(f"You lose your choice is {meaning[you]} and computer's is {meaning[computer]}")
        elif(computer == 2 and you == 1 ):
            print(f"You lose your choice is {meaning[you]} and computer's is {meaning[computer]}")
        elif(computer == 2 and you == 3 ):
            print(f"You win your choice is {meaning[you]} and computer's is {meaning[computer]}")      
        elif(computer == 3 and you == 1 ):
           print(f"You win your choice is {meaning[you]} and computer's is {meaning[computer]}") 
        else:
            print(f"You lose your choice is {meaning[you]} and computer's is {meaning[computer]}")                   
    play_again = input("Play again? (y/n): ").lower()
    print("Thanks for playing!")
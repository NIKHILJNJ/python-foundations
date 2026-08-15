from random import randint


class GuessGame:
    def __init__(self, usernumber):
        self.guess = usernumber
        self.target = randint(0, 1000)
        if self.guess == self.target:
            print("You guessed it! The number was", self.target )
        elif abs(self.guess - self.target) > 250:
            print("far from the target number The number was", self.target)
        elif abs(self.guess - self.target) > 150:
            print("somewhat close from the target number The number was", self.target)
        elif abs(self.guess - self.target) > 75:
            print("very close from the target number The number was", self.target)
        elif abs(self.guess - self.target) > 25:
            print("extremely close from the target number The number was", self.target )
        else:
            print("nailed it")

play_again = "y"

while play_again == "y":
    game = GuessGame(float(input("Enter your guess between 0 and 1000: ")))
    play_again = input("Play again? (y/n): ").lower()
    print("Thanks for playing!")



# My first logic after seeing the question but it is good for percentage base problem but not for this problem because the target number is a actual goal not a percentage.
#                print("Your guess is far from the target number. Better luck next time! The number was", self.target)
#            elif self.guess < self.target - self.target/3 or self.guess > self.target+self.target/3:
#               print("Your guess is somewhat close to the target number. Keep trying! The number was", self.target)
#          elif self.guess < self.target - self.target/4 or self.guess > self.target+self.target/4:
#             print("Your guess is very close to the target number. You're almost there! The number was", self.target)
#        elif self.guess < self.target - self.target/5 or self.guess > self.target+self.target/5:
#           print("Your guess is extremely close to the target number. You're so close! The number was", self.target)
#      else:
#         print("your guess is very close to the target number. You're almost there! The number was", self.target)            
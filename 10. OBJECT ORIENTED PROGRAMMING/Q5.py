class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Train Name: {self.name}")
        print(f"Total Seats: {self.seats}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}.")
            self.seats -= 1
            
        else:
            print("Sorry, no seats available.")

    def cancelTicket(self):
        print("Your ticket has been cancelled.")
        self.seats += 1

    def getFareInfo(self):
        print(f"The fare of the train is: {self.fare}")

train_name = input("Enter the name of the train: ")
train_fare = float(input("Enter the fare of the train: "))
train_seats = int(input("Enter the total number of seats in the train: "))

railway = train(train_name,train_fare,train_seats)


running = True
while running:
    choice = int(input(f"\n1: Book | 2: Cancel | 3: Status | 4: Fare | 5: Exit\nEnter choice: "))

    if choice == 1:
     railway.bookTicket()
    elif choice == 2:
        railway.cancelTicket()
    elif choice == 3:
        railway.getStatus()
    elif choice == 4:
     railway.getFareInfo()
    elif choice == 5:
     running = False
     print("Thank you for using the Nikhil's Railway Booking System")
    else:
        print("Invalid choice. Try again")      
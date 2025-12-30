from random import randint

class Train:

    def __init__(self, trainno):
        self.trainno = trainno
        
    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainno} from {fro} to {to}")

    def getStatus(self):
        print(f"Ticket in train no {self.trainno} is booked successfully")

    def getFare(self, fro, to):
        print(
            f"Ticket fare for train no {self.trainno} from {fro} to {to} is ₹{randint(222, 5555)}"
        )


t = Train(13425)
t.book("Kolkata", "Lalgola")
t.getStatus()
t.getFare("Kolkata", "Lalgola")

from datetime import datetime


# Every Transaction will have the information from a user

class Transaction:
    points: int
    payer: str
    date: datetime
    data = dict

    def __init__(self, date, payer):
        self.date = date
        self.payer = payer
        self.points = 0

    def add_transaction(self, points):
        self.points += points

    def to_string(self):
        return str(self.points) + str(self.payer) + str(self.date)

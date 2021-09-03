"""
This class represents a transaction that every user has
and it will contain information about their the payer, points, and date
"""
from datetime import datetime


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

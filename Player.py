#player class
class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}"      
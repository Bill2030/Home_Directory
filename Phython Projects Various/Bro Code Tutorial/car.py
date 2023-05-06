class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def car_driving(self):
        return "The car is driving"
    def car_stopped(self):
        return "The car is stopped"
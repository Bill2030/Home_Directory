from turtle import Turtle, Screen
class Turtle:
    def __init__(self, size, name):
        self.name= name
turtle = Turtle

screen = Screen()
screen.screensize(600, 400)
screen.bgcolor("black")

screen.exitonclick()


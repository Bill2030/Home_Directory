from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="While turtle color win race")
colors = ['red','green','blue','orange','indigo','violet']
y_positions = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230,y=y_positions[turtle_index])


screen.exitonclick()



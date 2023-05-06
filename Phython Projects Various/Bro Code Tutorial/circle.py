import turtle
tim = turtle.Turtle()
import random
color = ['red','green','purple','yellow','orange','violet','indigo','black']
turtle.speed("fastest")
for _ in range(200):
    turtle.color(random.choice(color))
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 10)






turtle.exitonclick()


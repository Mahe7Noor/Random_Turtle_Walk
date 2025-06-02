from turtle import Turtle, Screen
import random


timmy = Turtle()
screen = Screen()
direction = [0,90,180,270]

timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
   timmy.forward(10)
timmy.setheading(random.choice(direction))
    


screen.exitonclick()

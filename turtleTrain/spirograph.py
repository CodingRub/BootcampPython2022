import turtle as t
from random import randint, choice

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")

def draw_spirograph(gap: int):
    for i in range(int(360/gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)

draw_spirograph(0.5)
import turtle as t
from random import randint, choice

direction = [0, 90, 180, 270]
turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
turtle.pensize(10)
turtle.speed("fast")
for i in range(500):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.forward(30)
    turtle.setheading(choice(direction))
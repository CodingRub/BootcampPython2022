from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(30)

def move_backwards():
    t.backward(30)

def move_left():
    t.setheading(t.heading() + 10)

def move_right():
    t.setheading(t.heading() - 10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="r", fun=clear)
screen.exitonclick()


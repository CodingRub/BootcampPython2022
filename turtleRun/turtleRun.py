from turtle import Turtle, Screen, title
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle = []
y = -75
for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y)
    y += 30
    turtle.append(t)

running = True
while running:
    for i in turtle:
        i.forward(randint(0, 10))
        if i.pos()[0] > 230:
            color_win = i.color()[0]
            if color_win == user_bet:
                print("Congrats, Your {color_win} turtle is the winner !")
            else:
                print(f"Loser ! The {color_win} turtle is the winner !")
            running = False




screen.exitonclick()
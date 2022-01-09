from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")

screen.onkeypress(paddle_l.go_up, "z")
screen.onkeypress(paddle_l.go_down, "s")

running = True
while running:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
    if ball.xcor() > 345:
        ball.reset()
        score.l_point()
    if ball.xcor() < -345:
        ball.reset()
        score.r_point()
screen.exitonclick()
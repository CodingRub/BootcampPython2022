from turtle import Screen, Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX, newY)

    def bounce_y(self):
        self.y_move *= -1
        self.speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()
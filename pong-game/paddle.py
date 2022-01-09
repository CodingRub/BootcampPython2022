from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, pos: tuple):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, pos: tuple):
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def go_up(self):
        newY = self.ycor() + 50
        self.goto(self.xcor(), newY)

    def go_down(self):
        newY = self.ycor() -50
        self.goto(self.xcor(), newY)

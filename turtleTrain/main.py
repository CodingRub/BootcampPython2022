from turtle import *
from random import choice

def square(taille: int, color: str):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    for i in range(4):
        turtle.forward(taille)
        turtle.right(90)

def figure(side: int, taille: int, color: str):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    for i in range(side):
        turtle.right(360/side)
        turtle.forward(taille)

def dashedLine(taille: int, color: str):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    for i in range(30):
        turtle.forward(taille)
        turtle.penup()
        turtle.forward(taille)
        turtle.pendown()



colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(3, 11):
    figure(i, 100, choice(colours))
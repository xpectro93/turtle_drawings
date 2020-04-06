import turtle
import random
import math
wn = turtle.Screen()
wn.bgcolor('black')

turtle.pensize(3)
turtle.speed(0)
turtle.colormode(255)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()


def test(size):
    if size <= 15:
        return
    else:
        for i in range(5):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            turtle.pencolor(r,g,b)
            turtle.forward(size)
            test(size/2)
            turtle.left(216)
test(200)
while True:
    wn.update()
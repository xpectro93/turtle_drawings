import turtle
import random


loadWindow = turtle.Screen()
loadWindow.setup(width=1000, height=1000)
loadWindow.bgcolor("black")
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(3)

def draw_grid(STEP,LENGTH,COLOR):
    circleStart = 0
    for i in range(-500, LENGTH, STEP):
        if COLOR:

            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            turtle.pencolor(r,g,b)
        else:
            turtle.pencolor('black')

        #vertical lines 
        turtle.penup()
        #start position
        turtle.setpos(-500, LENGTH/2)
        turtle.pendown()
        #ending position
        turtle.setpos(-LENGTH/2 + i, -LENGTH/2)

        #horizontal lines
        turtle.penup()
        #start position
        turtle.setpos(LENGTH/2, -400)
        turtle.pendown()
        #ending position
        turtle.setpos(-500, -LENGTH/2 + i)
        turtle.goto(0,0)
        turtle.circle(circleStart+i)

x = 25
y = 800
color = True

while x > 0 or y < 0:
    draw_grid(x,y,color)
    color = not color
    loadWindow.update()
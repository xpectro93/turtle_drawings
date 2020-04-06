import turtle
import random


loadWindow = turtle.Screen()
loadWindow.setup(width=1000, height=1000)
loadWindow.bgcolor("black")
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(1)

def draw_grid(STEP,LENGTH):
    for i in range(-400, LENGTH, STEP):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.pencolor(r,g,b)


        #vertical lines 
        turtle.penup()
        #start position
        turtle.setpos(-400, LENGTH/2)
        turtle.pendown()
        #ending position
        turtle.setpos(-LENGTH/2 + i, -LENGTH/2)

        #horizontal lines
        turtle.penup()
        #start position
        turtle.setpos(LENGTH/2, -400)
        turtle.pendown()
        #ending position
        turtle.setpos(-400, -LENGTH/2 + i)

# draw_grid(25,800)
x = 100
y = 1000
while x > 0 or y < 0:
    draw_grid(x,y)
    x-= 5
    y-= 5
    loadWindow.update()
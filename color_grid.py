import turtle
import random


loadWindow = turtle.Screen()
loadWindow.setup(width=1000, height=1000)
loadWindow.bgcolor("black")
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(3)

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

loadWindow.listen()

hasDrawing = False
loadWindow.onclick(lambda :draw_grid(25,800))
while True:
    
    loadWindow.update()
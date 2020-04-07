import turtle

wn = turtle.Screen()
wn.title("Snake Test")
wn.bgcolor('black')

wn.setup(width=1000, height=1000)

pen = turtle.Turtle()
pen.penup()
pen.goto(0,400)
pen.pensize(5)
pen.speed(5)
pen.color('red')
pen.pendown()
pen.goto(175,-75)
pen.goto(-250,250)
pen.goto(250,250)
pen.goto(-175,-75)
pen.goto(0,400)
pen.speed(7)
pen.penup()
pen.goto(0,375)
pen.pendown()
pen.circle(-238)


pen.speed(0)
pen.penup()
pen.goto(0,-375)
pen.pendown()
pen.write("Made by: Don Jon", align='center', font=('Courier', 24, "normal") )


while True:
    wn.update()
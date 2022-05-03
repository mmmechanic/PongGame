import turtle
import os
import random


wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=1440, height=900)
wn.tracer(0)


# Score
sa = 0
sb = 0

# ruta
ru = turtle.Turtle()
ru.speed(0)
ru.color("white")
ru.penup()
ru.goto(-400, -300)
ru.pendown()
ru.goto(-400, 300)
ru.goto(400, 300)
ru.goto(400, -300)
ru.goto(-400, -300)
ru.hideturtle()

# Paddle A
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5, stretch_len=1)
pa.penup()
pa.goto(-350, 0)

# paddle b
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5, stretch_len=1)
pb.penup()
pb.goto(350, 0)

# ball
pl = turtle.Turtle()
pl.speed(0)
pl.shape("circle")
pl.color("white")
pl.penup()
pl.goto(0, 0)
pl.dx = 1
pl.dy = 1
div = 10


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  player B: 0", align="center", font=("Courier", 24, "normal"))


def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)


def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)


def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)

def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)


wn.listen()
#wn.onkeypress(pa_up, "w")
#wn.onkeypress(pa_down, "s")
wn.onkeypress(pb_up, "Up")
wn.onkeypress(pb_down, "Down")


# main game loop
while True:
    wn.update()

    # move the ball
    if div == 0:
        div = 1
        pl.setx(pl.xcor() + pl.dx)
        pl.sety(pl.ycor() + pl.dy)
    else:
        div = div - 1

    # ai
    slumptal = random.randint(0, 100)
    if slumptal < 5:
        if pa.ycor() < pl.ycor():
            pa_up()



        else:
            pa_down()





    # border checking

    if pl.ycor() > 290:
        pl.sety(290)
        pl.dy *= -1
        os.system("aplay bonk-sound-effect.wav&")

    if pl.ycor() < -290:
        pl.sety(-290)
        pl.dy *= -1
        os.system("aplay bonk-sound-effect.wav&")

    if pl.xcor() > 390:
        pl.goto(0,0)
        pl.dx *= -1
        sa += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(sa, sb), align="center", font=("Courier", 24, "normal"))


    if pl.xcor() < -390:
        pl.goto(0, 0)
        pl.dx *= -1
        sb += 1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(sa, sb), align="center", font=("Courier", 24, "normal"))



    # colition ball and paddle

    if (pl.xcor() > 340 and pl.xcor() < 350) and (pl.ycor() < pb.ycor() + 40 and pl.ycor() > pb.ycor() -40):
        pl.setx(340)
        pl.dx *= -1
        os.system("aplay bonk-sound-effect.wav&")

    if (pl.xcor() < -340 and pl.xcor() > -350) and (pl.ycor() < pa.ycor() + 40 and pl.ycor() > pa.ycor() - 40):
        pl.setx(-340)
        pl.dx *= -1
        os.system("aplay bonk-sound-effect.wav&")

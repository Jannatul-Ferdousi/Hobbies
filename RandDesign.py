import turtle
from turtle import *
from random import randint
speed(0) #drawing speed
bgcolor("black")

x=1
while x<400:
    r = randint(0,255)
    g= randint(0,255)
    b = randint(0, 255)
    colormode(255)
    pencolor(r,g,b)
    fd(50+x)
    rt(90.911)
    #rt(300)
    x+=1
exitonclick()


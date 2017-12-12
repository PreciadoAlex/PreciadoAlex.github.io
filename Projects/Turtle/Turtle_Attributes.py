import turtle

Turt = turtle.Screen()
Turt.colormode(255)
Turt.bgcolor(0,0,0)
r=255
b=0
g=0


def Speed_Square():
    for i in range (10):
        turtle.speed (i)
        turtle.forward (100 + i)
        turtle.left (90)
        turtle.forward (100 + i)
        turtle.left (90)
        turtle.forward (100 + i)
        turtle.left (90)
        turtle.forward (100 + i)
        turtle.left (90)
#Speed_Square()

def colorsquare(r,g,b):
    for i in range(4):
        turtle.color(r,g,b)
        turtle.forward(50)
        turtle.right(90)
        r =r-50
        b=b+50
        g=g+50
colorsquare(r,g,b)

    

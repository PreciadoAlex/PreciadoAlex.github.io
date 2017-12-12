import turtle
import time
#turtle.speed (0)
def Square():
    x = 0
    for i in range (30):
        x = x + 25
        for i in range (4):
            turtle.forward (25 + x)
            turtle.left (90)
Jon = turtle.Turtle()
#Square()
def center():
    y = 0
    z = 0
    for i in range(20):
        Jon.penup()
        Jon.goto(-z, -z)
        Jon.pendown()
        z = z + 12.5
        y = y + 25
        for i in range (4):
            Jon.forward (25 + y)
            Jon.left (90)
#center()
def poly():
    side = 3
    for i in range (20):
        for i in range (side):
            turtle.forward (25)
            turtle.left(360/side)
        side = side + 1
poly()
        

            
    

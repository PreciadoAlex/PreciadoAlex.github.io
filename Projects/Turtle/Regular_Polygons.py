from turtle import forward, left, speed

speed = 200

def quad():
    for i in range (4):
        forward (100)
        left (90)
def tri():
    for i in range (3):
        forward (100)
        left (120)
def hex():
    for i in range (6):
        forward (100)
        left(60)
def non():
    for i in range (9):
        forward (100)
        left (360/9)
def dec():
    for i in range (10):
        forward (100)
        left (36)
quad()
tri()
hex()
non()
dec()
def AnyRegPoly():
    side = int(input('Hello user. How many sides do you want your polyon to have? '))
    size = int(input('Great! Now choose the size of your polygon. '))
    for i in range (side):
        forward (size)
        left (360/side)
AnyRegPoly()

    

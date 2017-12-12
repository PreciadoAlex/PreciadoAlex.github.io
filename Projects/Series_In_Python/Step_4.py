# cosine function using degrees
import math
pi = math.pi
x = int(input("select a number: "))
f = s.lower(input ('please enter either D for Degrees or R for Radians: '))
if f == 'd':
    def cosine(x):
        y = 1 - ((x**2/2) + (x**4/24) - (x**6/720) + (x**8/40320))/math.factorial(2)
        y = y *180/pi
        return y


    print (cosine(0))
    print (cosine(pi/2))
    print (cosine(pi))
if f == 'r':
    def cosine(x):
        y = 1 - ((x**2/2) + (x**4/24) - (x**6/720) + (x**8/40320))/math.factorial(2)
        return y


    print (cosine(0))
    print (cosine(pi/2))
    print (cosine(pi))

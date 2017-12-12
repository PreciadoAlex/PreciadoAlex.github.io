import time
print ("Hello user! Please pick a number")
x = int(input())

while x > -1:
    print (x)
    x = x - 1
    time.sleep (1)
print ("Timer Done!")

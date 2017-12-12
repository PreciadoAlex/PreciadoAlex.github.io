import time
print ("Hello user! Please pick a number, preferrably a large one.")
x = int(input())
for i in range (x, 0, -1):
    print (i)
    time.sleep (1)
print ("Timer done!")

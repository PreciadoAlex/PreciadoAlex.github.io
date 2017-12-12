def rec():
    x = 1
    J = int(input('please enter a number: '))
    y = 3
    F = 0
    for i in range (J):
        print (x, end=" + ")
        x = x * y
        F = F + x
    print (0)
    print ("""
the sum of your series is""", F)
rec()

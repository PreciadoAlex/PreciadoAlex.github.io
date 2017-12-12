def fib(n):
    first = 1
    second = 1
    sume = 2
    print(first)
    print (second)
    for i in range (n-2):
        third = first + second
        print (third)
        first = second
        second = third
        sume = sume + third

    print ("the sum of your sequence is:" , sume)
j = int(input("How many numbers into Fibonacci do you want to go? "))
fib(j)

    

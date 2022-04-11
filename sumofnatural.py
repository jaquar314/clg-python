def nat():
    a=int(input("enter a number:"))
    if a< 0:
        print("Enter a positive number")
    else:
        sum = 0
        while (a > 0):
            sum += a
            a -= 1
        print("The sum is", sum)
nat()

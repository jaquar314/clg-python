print("Enter Your Choice 1(Add)/2(Sub)/3(Divide)/4(Multiply)")
num = int(input())
if num == 1:
    print("Enter Number 1 : ")
    add1  = int(input())
    print("Enter Number 2 : ")
    add2 = int(input())
    sum = add1 + add2
    print("The Sum Is ", sum)
elif num == 2:
    print("Enter Number 1 : ")
    sub1  = int(input())
    print("Enter Number 2 : ")
    sub2 = int(input())
    difference = sub1 - sub2
    print("The Difference Is ", difference)
elif num == 3:
    print("Enter Number 1 : ")
    div1  = float(input())
    print("Enter Number 2 : ")
    div2 = float(input())
    division = div1 / div2
    print("The Division Is ", division)
elif num == 4:
    print("Enter Number 1 : ")
    mul1 = int(input())
    print("Enter Number 2 : ")
    mul2 = int(input())
    multiply = mul1 * mul2
    print("The Difference Is ", multiply)
else:
    print("enter a valid Number")
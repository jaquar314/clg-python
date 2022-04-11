def amstrong():
    r=0
    x=int(input("enter the number:"))
    num=x
    while(x>0):
        temp=x%10
        r+=temp*temp*temp
        x=x//10
    if(num==r):
        print("it is a amstrong number")
    else:
        print("it is not a amstrong")
amstrong()
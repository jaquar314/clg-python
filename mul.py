def mul(a,b):
    if a==0 and b==0:
        return 0
    return(a+mul(a,b-1))
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
print(mul(a,b))


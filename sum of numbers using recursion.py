def add(a,b):
    if b==0:
        return a
    return(1+add(a,b-1))
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
print(add(a,b))


def sod(a):
    if(a==0):
        return 0
    return (a%10+ sod(int(a/10)))
a=int(input("enter the value :"))
print(sod(a))
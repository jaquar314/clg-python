def natural(n):
    su=0
    i=1
    print("natural numbers from",i,"to",n+1)
    for i in range(i,n+1):
        su+= i
    print(su)
x=int(input("enter the number:"))
natural(x)
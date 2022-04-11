def prime(n):
    for i in range(1,n+1):
        if(i>1):
            for p in range(2,i):
                if i%p==0:
                    break
            else:
                print(i,end=' ')
a=int(input("enter the number"))
prime(a)
def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return n
    return fib(n-1)+ fib(n-2)
x=int(input("enter the number :"))
print(fib(x))
for i in range(x):
    print(fib(i),end=" ")
n=int(input("enter the number"))
rev=0
while(n>0):
    temp=n%10
    rev=rev*10+temp
    n=n//10
print("the reversal of the number:",rev)

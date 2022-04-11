  def palindrome():
    rev=0
    x=int(input("enter the number:"))
    num=x
    while(x>0):
        temp=x%10
        rev=rev*10+temp
        x=x//10
    if(num==rev):
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

palindrome()
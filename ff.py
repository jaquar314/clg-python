string="My Name Is Saikiran"
vowels=0
space=0
digits=0
upper=0
lower=0
for i in range(0,len(string)):
    ch=string[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' ):
        vowels+=1
print(vowels)
for i in range(0 , len(string)):
    ch=string[i]
    if( string[i]== " " ):
        space+=1
print(space)
for i in range(0,len(string)):
    digits+=1
print(digits)
for i in string :
    if(i.islower()):
        lower+=1
print("the no of the lower case letters are :",lower)
for i in string:
    if(i.isupper()):
        upper+=1
print("the no of upper case letters are :",upper)
res = len(string.split())
print("the no of words are :"+str(res))



str=input("enter the string:")
vowels=0
space=0
digits=0
consonants=0
for i in range(0,len(str)):
    ch=str[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' ):
        vowels+=1
    else:
        consonants+=1
print("the no of consonants in the word is:",consonants)
print("the no of vowels in the word is:",vowels)
for i in range(0,len(str)):
    ch=str[i]
    if(str[i]==" "):
        space+=1
print("the no of blank spaces in the string is:",space)
for i in range(0,len(str)):
    digits+=1
print("the no of digits in the string is:",digits)




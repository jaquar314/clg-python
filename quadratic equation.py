def quad():
    while True:
        a= int(input("enter the first co-ordinate"))
        if(a==0):
            print("invalid number")
        else:
            break
    b = int(input("enter the second co-ordinate"))
    c= int(input("enter the third co-ordinate"))
    d=(b*b)-(4*a*c)
    den=2*a
    srv=pow(d,0.5)
    if(d>0):
        print("real roots and differnt")
        root1=(-b+d**0.5)/den
        root2=(-b-d**0.5)/den
        print("root 1=",root1,"root2=",root2)
    elif(d==0):
        print("equal roots")
        root1=-b/den
        print("root1 and root2 are=",root1)
    else:
        print("imaginary roots")
        print(-b/(2*a),"+i",srv)
        print(-b/(2*a),"-i",srv)
quad()

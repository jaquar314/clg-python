def cbr(list):
    list.append(50)
    print("inside function:",list)
list=[10,20,30,40,]
cbr(list)
print("outside function:",list)
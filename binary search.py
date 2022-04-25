def binarySearchAlgo(xlist, key):
    a = 0
    b = len(xlist)
    while a < b:
        c = (a + b) // 2
        if xlist[c] > key:
            b = c
        elif xlist[c] < key:
            a = c + 1
        else:
            return c
    return -1


# input a list of elements
xlist = input('Enter the sorted list of numbers: ')

# split a element
xlist = xlist.split()
xlist = [int(x) for x in xlist]

# search for in list
key = int(input('The number to search for: '))

# call binary search function
index = binarySearchAlgo(xlist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))

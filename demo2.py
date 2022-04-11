# importing the module
import sys

# storing the arguments
program = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

# displaying the program name
print("Program name : " + program)

# displaying the arguments
print("arg1 : " + arg1)
print("arg2 : " + arg2)
print("arg3 : " + arg3)
print("Number of arguments : ", len(sys.argv))
print(sys.argv)

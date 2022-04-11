# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class profile:
	clas= 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = profile('sai', 1)
b = profile('kiran', 2)

print(a.clas) # prints "cse"
print(b.clas) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(profile.clas) # prints "cse"

# Now if we change the clas for just a it won't be changed for b
a.clas = 'ece'
print(a.clas) # prints 'ece'
print(b.clas) # prints 'cse'

# To change the clas for all instances of the class we can change it
# directly from the class
profile.clas = 'mech'

print(a.clas) # prints 'ece'
print(b.clas) # prints 'mech'

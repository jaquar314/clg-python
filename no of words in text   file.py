# creating variable to store the
# number of words
number_of_words = 0

# Opening our text file in read only
# mode using the open() function
with open(r'sai.txt','r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Splitting the data into separate lines
	# using the split() function
	lines = data.split()

	# Iterating over every word in
	# lines
	for word in lines:

		# checking if the word is numeric or not
		if not word.isnumeric():

			# Adding the length of the
			# lines in our number_of_words
			# variable
			number_of_words += 1

# Printing total number of words
print(number_of_words)

# Open the file in read mode
text = open("sai.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
	# Remove the leading spaces and newline character
	line = line.strip()

	# Convert the characters in line to
	# lowercase to avoid case mismatch
	line = line.lower()

	# Split the line into words
	words = line.split(" ")

	# Iterate over each word in line
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			# Increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, ":", d[key])

# Example: Finding the mode of a list of values.
# The mode of a list of values is the value that appears most frequently.
# The following script inputs a list of words from a text file and prints their mode.

fileName = input("Enter the filename: ")
f = open(fileName, "r")

# Input the text, convert its words to uppercase, and add the words to a list
words = []
for line in f:
    for word in line.split():
        words.append(word.upper())

# Obtain unique words and frequencies, saving thses in a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:  # word encountered for the first time
        theDictionary[word] = 1
    else:   # word was already seen, increment its number
        theDictionary[word] = number + 1

# Find the mode by obtaining max value in dictionary and determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break
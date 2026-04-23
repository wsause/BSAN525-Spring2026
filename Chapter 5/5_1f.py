# Note that the code uses a for loop over an index rather than
# a for loop over the list of elements, because the index is needed
# to access the positions for the replacements.

sentence = "This example has five words."
words = sentence.split()    # Creates a list from a string

for index in range(len(words)):
    words[index] = words[index].upper()

print(words)
# Python includes a set of string operations called methods that 
# make tasks like counting the words in a single sentence easy.

sentence = input("Enter a sentence: ")
listOfWords = sentence.split()  # breaks sentence into list of words
print("There are", len(listOfWords), "words.")

sum = 0
for word in listOfWords:
    sum += len(word)
print("The average word length is", sum / len(listOfWords))

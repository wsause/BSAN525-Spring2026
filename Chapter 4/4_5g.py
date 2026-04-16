# The next code segment modifies the previous example
# to handle integers separated by spaces and/or newlines

f = open("integers.txt", "r")

theSum = 0
numbers = f.read()
wordList = numbers.split()
for word in wordList:
    number = int(word)
    theSum += number
print("The sum is", theSum)
f.close()
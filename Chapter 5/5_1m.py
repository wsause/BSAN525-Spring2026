"""
Researchers who do quantative analysis are
often interested in the median of a set of numbers.
Median - the value that is less than half the numbers
in the set and greater than the other half.
"""

fileName = input("Enter the filename: ")
f = open(fileName, "r")

# Input the text, convert it to numbers, and add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(word)
numbers.sort()
midpoint = len(numbers) // 2
print("The median is", end=" ")
if len(numbers) % 2 == 1:   # if len of list is odd
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

f.close()
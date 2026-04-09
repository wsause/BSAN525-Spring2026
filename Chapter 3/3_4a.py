"""
The for loop executes a set of statements a definite number of times.
In many situations, however, the number of iterations in a loop is unpredictable.
The while loop can be used to describe conditional iteration, meaning
the process continues to repeat as long as a consition remains true.
"""

# For example, a program's input loop can accept values until
# the user enters a sentinel that terminates the input
theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":   # the user did not press enter
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)
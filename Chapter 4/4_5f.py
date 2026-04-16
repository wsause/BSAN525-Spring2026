# string representations of integers and floating-point
# numbers can be converted to number by useing the
# functions int and float

f = open("integers.txt", "r")

theSum = 0
for line in f:
    # line = line.strip() # removes '\n' (not necessary)
    number = int(line)
    theSum += number
print("The sum is", theSum)
f.close()

"""
In scripts that include the definitions of several
cooperating functions, it is often useful to define
a speacial function named main that serves as the entry
point for the script.
"""

def square(x):
    return x * x

def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

main()
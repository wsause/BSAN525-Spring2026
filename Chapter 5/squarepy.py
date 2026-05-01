def square(x):
    return x * x

def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

# The entry point for program execution.
# Must be called at the end of the script
if __name__ == "__main__":  # if running as a standalone program
    main()
# len and [] work on lists as they do for strings
first = [1, 2, 3, 4]
print(len(first))
print(first[0])
print(first[2:4])


# Concatenation (+) and equality (==) also work as expected for lists
first = [1, 2, 3, 4]
second = list(range(1, 5))
print(first + [5, 6])
print(first == second)


# The in detects the presnece of an element
print(3 in [1, 2, 3])
print(0 in [1, 2, 3])

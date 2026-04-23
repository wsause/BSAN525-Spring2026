# extend performs a similar operation, but adds the
# elements of its list argument to the end of the list
example = [1, 2, 3]
example.extend([11, 12, 13])
print(example)

# The method pop is used to remove an element at a given position
example.pop()   # Remove the last element
print(example)
example.pop(0)  # Remove the first element
print(example)

example.remove(11)
print(example)
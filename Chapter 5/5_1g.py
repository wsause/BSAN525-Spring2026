"""
The list type incudes several methods for
inserting and removing elements.
The method insert expects an integer index
and the new element as argements.
"""

example = [1, 2]
example.insert(1, 10)
print(example)

example.insert(3, 25)
print(example)


# append expects a new element as an argument and
# adds it to the end of the list
example = [1, 2]
example.append(3)
print(example)
"""
Python includes many useful functions,
which are organized in libraries of code called modules.
Functions ofter require arguments,
referred to by names known as parameters
"""

# The math module includes functions that
# perform basic mathematical operations
import math

print(math.pi)
print(math.sqrt(2))


"""
If you are going to use only a couple of a module's resources,
you can just import the individual resources,
which saves memory and makes your program run faster.
"""
from math import sqrt, pi

print(pi)
print(sqrt(2))
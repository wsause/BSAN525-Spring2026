"""
All of the functions and methods examined in the previous chapters return
a value that the called can then use to complete its work.
Mutator methods (e.g., insert, append, extend, pop, and sort) usually
return no value of interest to the caller.
"""

aList = [4, 2, 10, 8]
aList = aList.sort()
print(aList)

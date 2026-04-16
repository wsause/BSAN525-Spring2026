"""
Ceaser cipher replaces each character in plain text with a
character a given distance away.
The ord function returns the oprdinal position in the ASCII sequence.
chr is the invers function.
"""

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""

for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord("z"):
        cipherValue = ord("a") + distance - (ord("z") - ordvalue + 1)
    code = code + chr(cipherValue)

print(code) 

# A Boolean function usually tests its argument for the
# presence or absence of some property

def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False
    
print(odd(5))
print(odd(6))
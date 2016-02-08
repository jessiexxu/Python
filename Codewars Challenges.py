# Challenge 1. Categorize New Memeber
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
# They would like your help with an application form that will tell prospective members which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Solution I:
def openOrSenior(data):
    output = []
    for i in data:
        if i[0] > 54 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output

# Solution II:
def openOrSenior(data):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in data]

###
# Challenge 2. You are a square!
# Given an integral number, determine if it's a square number.

# Solution I:
def is_square(n):   
    if n <= 0:
        return False
    else:
        return n%n**0.5==0

# Solution II:
def is_square(n):
    return n > 0 and (n**0.5).is_integer()

###
# Challenge 3. Triangular Treasure
# Return the nth triangular number.
def triangular(n):
    if n <1:
        return 0
    else:
        return n*(n+1)/2


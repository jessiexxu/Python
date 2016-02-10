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

###
# Challenge 4. Good vs Evil
# Good: Hobbits - 1, Men - 2, Elves - 3, Dwarves - 3, Eagles - 4, Wizards - 10
# Evil: Orcs - 1, Men - 2, Wargs - 2, Goblins - 2, Uruk Hai - 3, Trolls - 5, Wizards - 10
# Input the count of each parameter and output the result of the battle

def goodVsEvil(good, evil):
    result = {'good': 'Battle Result: Good triumphs over Evil', 
              'evil': 'Battle Result: Evil eradicates all trace of Good',
              'tie': 'Battle Result: No victor on this battle field'}
    good_value = [1,2,3,3,4,10]
    evil_value = [1,2,2,2,3,5,10]
    good_sum = sum([int(x)*y for x, y in zip(good.split(), good_value)])
    evil_sum = sum([int(x)*y for x, y in zip(evil.split(), evil_value)])

    if good_sum > evil_sum:
        return result['good']
    elif good_sum < evil_sum:
        return result['evil']
    else:
        return result['tie']

###
# Challenge 5. Does my number look big in this?
# A Narcissistic Number is a number which is the sum of its own digits, 
# each raised to the power of the number of digits.
# Return true or false depending upon whether the given number is a Narcissistic number.

def narcissistic(value):
    return sum(int(i)**len(str(value)) for i in str(value)) == value

###
# Challenge 6. Replace with alphabet position
# Input a text and return alphabet position for letters in the text

import string

def alphabet_position(text):
    out = []
    for i in text:
        if i.isalpha():
            out.append(string.lowercase.index(i.lower())+1)
    return ' '.join(map(str,out))

# OR

import string

def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower())+1) for letter in text if letter.isalpha()])

###
# Challenge 7. Array.diff
# Remove all values from list a, which are present in list b.

def array_diff(a, b):
    return [x for x in a if x not in b]

###
# Challenge 8. FInd the odd int
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    return [x for x in seq if seq.count(x)%2][0]

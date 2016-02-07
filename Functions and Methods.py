# Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
    volume = 4/3 * math.pi * rad**3
    return volume

print vol(4)

# Write a function that checks whether a number is in a given range (Inclusive of high and low).
def ran_check(num,low,high):
    if num in range (low, high+1):
        print "Yes"
    else:
        print "No"

ran_check(4,2,8)

# If you only wanted to return a boolean:
def ran_bool(num,low,high):
    return num in range (low, high+1)
    
ran_bool(3,1,10)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def up_low(s):
    d = {"upper": 0, "lower": 0}
    for letter in s:
        if letter.isupper():
            d["upper"] += 1
        elif letter.islower():
            d["lower"] += 1
        else:
            pass
    print "The string is: ", s
    print "No. of Upper case characters: ", d["upper"]
    print "No. of Lower case characters: ", d["lower"]

print up_low("THis is a test!")

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    output = list(set(l))
    return output

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

multiply([2,2,3,-4])

# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
    return s == s[::-1]

palindrome('helleh')

# Write a Python function to check whether a string is pangram or not.
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print alphaset
    return alphaset <= set(str1.lower())

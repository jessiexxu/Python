###### 1. Statements Assessment
# Use for, split(), and if to create a Statement that will print out letters that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print word

# Use range() to print all the even numbers from 0 to 10.
print range(1,10,2)

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisble by 3.
lst = [num for num in range(1,51) if num%3 == 0]
print lst

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print word + " <--even!"

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".
for i in range(1,101):
    if i%15 == 0:
        print 'FizzBuzz'
    elif i%3 == 0:
        print "Fizz"
    elif i%5 == 0:
        print 'Buzz'
    else:
        print i

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
lst = [letter[0] for letter in st.split()]
print lst


###### 2. Functions and Methods

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


###### 3. Errors and Exceptions

### Problem 1 Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print i**2
except:
    print "An error occurred!"

### Problem 2 Handle the exception thrown by the code below by using **try** and **except** blocks. 
### Then use a **finally** block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
except:
    print "integer division or modulo by zero"
finally:
    print "All Done."

### Problem 3 Write a function that asks for an integer and prints the square of it. 
### Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            num = input("Input an integer: ")
        except:
            print "An error occured! Please try again!"
            continue
        else: 
            break
        
    print "Thank you, you number squared is: ", num**2


###### 4. Object Oriented Programming

## Problem 1 Fill in the Line class methods to accept coordinate as a pair of 
## tuples and return the slope and distance of the line.
import math
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/float(x2-x1)

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

## Problem 2. Fill in the class
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return round(math.pi*self.radius**2*self.height,1)
    
    def surface_area(self):
        top = math.pi*self.radius**2
        return round(2*top + 2*math.pi*self.radius*self.height,1)

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()



###### 5. Battleship Game

# In this project I will build a simplified, one-player version of the classic board game Battleship! 
# There will be a single ship hidden in a random location on a 5x5 grid. 
# The player will have 4 guesses to try to sink the ship.

# Set up the 5x5 board and the actual location of the ship
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Have the player guess the ship's location then check if the player guessed right
# The player has 4 chances to sink the ship
for turn in range(4):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
    elif (board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    if turn == 3:
        print "Game Over"
        
    print_board(board)

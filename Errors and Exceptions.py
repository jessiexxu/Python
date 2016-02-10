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

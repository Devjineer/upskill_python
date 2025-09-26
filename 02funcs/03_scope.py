"""scope of a variable, is how accessible is a variable in execution of a program
their behaviour and accessibility depends on where they are declared;
"""

# LOCAL VARIABLE
"""variables that are only accessible in the block they are being declared"""


def greet():
    msg = "hello"
    print("inside function", msg)


greet()

# print('Outside function', msg)

# GLOBAL VARIABLES
"""Are declared outside all functions or blocks and can be accessed anywhere in the program"""
msg = "Python is awesome"


def display():
    print("Inside function", msg)


display()

print("Outside function", msg)

"""
If two variables of diff scope is declared the one with local scope overshadows the global
"""

x = 'i am x';
def callX():
    x = 'I am y';
    print(x);
callX()
print(x) # cannot change immutable value

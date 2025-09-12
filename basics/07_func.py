# FUNCTIONS
"""Block of code (statements) that does a specific task"""


def fun():
    print("Welcome to Python")


fun()


def evenOdd(number):
    if number is 0:
        return

    if number % 2 is not 0:
        print(f"{x} is an odd number")
    else:
        print(f"{x} is an even number")


for x in range(6):
    evenOdd(x)


# TYPE OF ARGUMENTS OR PARAMETERS
"""Default Arguments"""


def sum(x, y=50):
    print(x + y)


sum(2)

"""Keyword Arguments
call the function with the specified params so there is no error
"""
sum(y=100, x=200)

"""Positional Arguments"""
"""Call the function with values not specifying name of args, so values are assigned to parameters based on their order"""

sum(20, 30)
# x first, y second

print('************************************************************')
'''**args, takes it like dictionary'''
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


# Function call with both types of arguments
# myFun("Hey", "Welcome", first="Geeks", mid="for", last="Geeks")

#LAMBDA
sum = lambda x, y:  x + y
mySum = sum(30, 40);
# print(mySum)

#PASSING BY REFERENCE AND PASSING BY VALUE
x = 5;
def func(number):
    number += 10;
    # print(number)
func(x);
# print(x);

def func(arr):
    arr[0] = 20;
array = [1, 2, 3, 4];
func(array);
# print(array);

# RECURSIVE FUNCTION
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1);
# print(factorial(5)) 


def printing(stop, start = 0):
    if start <= stop:
        print(start);
        printing(stop, start + 1)
    else:
        return 0
    
# printing(5)

def summing(n, start = 0):
    if n == 10:
        return start;
    else:
        return summing(n + 1, start + n);
print(summing(8))
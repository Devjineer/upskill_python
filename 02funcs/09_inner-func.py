# Local Variables
def fun1():
    msg = "Josemaria"

    def fun2():
        print(msg)

    fun2()


fun1()


# modifying variables using nonlocal
def fun1():
    a = 45

    def fun2():
        nonlocal a  # this makes it no create a new local copy
        a = 54
        print(a)

    fun2()
    print(a)


fun1()


# closure in inner function
def fun1(a):
    def fun2(b):
        print(a + b)

    return fun2


fun1(2)(3)


def process_data(data):
    def clean_data():
        return [item.strip() for item in data]

    return clean_data()


print(process_data(["  python", "          INner function    "]))


import logging

logging.basicConfig(level=logging.INFO)


def logger(fn):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {fn.__name__} with {args}, {kwargs}")

    return wrapper



@logger
def add(a, b, key = 'jose'):
    
    return a + b;

sum = add(3, 2);

@logger
def subtract():
    print('subtract')

subtract()
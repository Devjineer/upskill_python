# Assigning function to a variable
def msg(name):
    return f'Hello {name}';

sayHi = msg;
print(sayHi('jose'))


# PASSING FUNCTIONS AS ARGUMENTS
def fun1(fn, name):
    return fn(name);

print(fun1(sayHi, 'Devjineer'))

# return functions from other functions

# STORING FUNC IN DATA STRUCTURES
def add(x, y):
    return x + y;
def subtract(x, y):
    return x - y;

operations = {
    'plus': add,
    'minus': subtract
}

print(operations['minus'](10, 5))
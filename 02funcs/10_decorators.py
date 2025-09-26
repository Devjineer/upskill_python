"""decorators are functions (higher order functions), that accept functions  as args and return a wrapper, wrapping the original function to enhance it by adding extra behaviour before and / or after execution of the function"""

"""We have mymethod_decorator this is used in classes for methods, but also take self"""


def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After function")

    return wrapper


@decorator
def consoles():
    print("Working with decorators")


consoles()


def decorator_name(fn):
    def wrapper(*args, **kwargs):
        print("Before Execution")
        print(kwargs, fn.__name__)
        result = fn(*args, **kwargs)
        print("After execution")
        return result

    return wrapper


@decorator_name
def add(a, b):
    return a + b


print(add(2, 3))

# @decorator_name: Syntax sugar for add = decorator_name(add).


# FUNCTIONS AS FIRST CLASS OBJECTS
# there can be treated like any other object or value


# Assigning a function to a variable
def greet(n):
    print(n)


sayHi = greet
sayHi("JOse")


# Passing a function as an argument
def apply(fn, name):
    fn(name)


apply(greet, "New name")


# types of decorators
# - function decorators
# - method decorators - work with self and args and kwargs
# - class decorators = for classes


def fun(cls):
    cls.className = cls.__name__
    return cls

@fun
class Person():
    pass

print(Person.className);
# REVIEW: will come back to decorators
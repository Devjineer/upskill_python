'''
Variables can be used to store data, that can be referenced and manipulated
during program execution. There are named storage for data.
Allows us to store and reuse values in our program

- No explicit declaration type
- Type is inferred based on value assigned

NAMING VARIABLES
- can only have letters and numbers and _(underscore);
- can not start with digit
- cannot use keywords in python
'''

# BASIC TYPING
x = 5;
y = 3.14;
z = 'Hi'

# DYNAMIC TYPING
'''means a variable can hold diff types of values during execution'''
x = 'hi';
x = 0.5e2


# CASTING VARIABLES
'''int(), float(), str()'''
x = int('123');
y = float(123);
z = str(12838);
print(x, y, z)

# GETTING TYPE OF VARIABLE OR DATA TYPE
'''type(variableName)'''
print(type(x), type(y), type(z))


# SHARED REFERENCE
'''Where multiple variables reference same value, it is known as shared reference'''
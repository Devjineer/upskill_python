# ARITHMETIC
"""+, -, %, /, *, //, **"""

# RELATIONAL (COMPARISON)
"""<, >, <=, >=, !=, =="""

# LOGICAL OPERATOR
"""AND, OR, NOT"""

# BITWISE OPERATOR
"""&, |, <<, >>, -, ^"""

# ASSIGNMENT OPERATORS
"""=, +=, *=, %=, /="""

a = True
print(not not a)

# IDENTITY OPERATORS
"""is, is not"""
a = 3
b = 3
c = 7
print(a is b)
print(a is c)
print(c is not a)

# MEMBERSHIP OPERATORS
"""in, not in"""
list1 = [3, 4, 5, 8]
print(a in list1)
print(c not in list1)

# TERNARY OPERATORS
x, y, z = input("Input 3 digits").split()
print(x, y, z)
min = (
    x
    if x < y and x < z
    else y if y < x and y < z else z if z < x and z < y else "no valid input"
)
print(min)

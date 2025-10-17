# TUPLE
"""Similar to list but immutable, ordered (indexed)"""

# CREATION
tpl = ("jose", "maria", "dee")
tpl2 = tuple(("1", 2, 3, "lake"))


# creating tuple by nesting tuples
tpl3 = (tpl, tpl2)
print(tpl3)


# create tuple with repetition
tpl4 = ("jose",) * 3
print(tpl4)

# Accessing tuples
# indexing
print(tpl[0])

# slicing
print(tpl2[2:])

# UNPACKING TUPLE
tpl = ("banana", "apple", "water melon")

a, *items = tpl;
print(a);
print(items)


# concatenation of tpl with the + operator
tpl = tpl2 + tpl;
print(tpl)


# slicing purple
print(tpl[::-1])

# deleting a tuple
# del tpl;
"""Strings are sequence of characters enclosed in quotes(single or double quotes)
it can include letters, numbers, symbols or space.
they are widely used for text handling and manipulation.
"""

# CREATING A STRING
str = "Hello GFG"
print(str)

multilineStr = """This is multiline
string"""
print(multilineStr)

"""ACCESSING STRINGS"""
"""Strings are indexed sequences
Positive indices starts from the right at 0 
Negative indices starts from the left at -1
"""
str = "GEEKS FOR GEEKS"

# positive indexing
print(str[0], str[4])

# negative indexing
print(str[-1], str[-5])


# STRING SLICING
# A way to extract a portion of string by specifying the start and end indexes
# The syntax is string[start:end]
str = "GEEKS FOR GEEKS"
print(str[1:4])
print(str[:3])  # this is from the start to but excluding index 3
print(str[3:])  # this is from index 3 to end
print(str[::-1])  # this is to reverse the string
print(str[::-2])  # this is to reverse the string jumping 2nd char

# STRING ITERATION
# we can loop through strings, because there are iterable
s = "python"
for char in s:
    print(char)

# STRING IMMUTABILITY
# strings cannot be changed when created, we can only create new strings from the original
# if we need to manipulate strings we can only use the string methods slice, concatenation or formatting to create new strings based on the original

s = "geeks for geeks"
print(s)
s = "G" + s[1:]
print(s)


# DELETING A STRING
delStr = "the string to be deleted"
print(delStr)
del delStr
# print(delStr); # throws an error

# UPDATING STRINGS
str = "hello Geeks"
str = str[:6].upper() + "g" + str[7:]
print(str)


print(str.replace("geeks", "People"))

# COMMON STRING METHODS
common_string = "common string"
print(len(common_string))  # the length of the string
print(common_string.upper())
print(common_string.lower())
print(common_string.capitalize())

text2 = "      JOSE    "
print(text2.strip())
# remove trailing and leading whitespace

text3 = "hello geeks, this is where geeks come to geeks geeksable things out"
print(
    text3.replace("geeks", "people")
)  # replace all occurrences of a specified substr with another

print(
    "Concatenation"
    + " "
    + "is done"
    + " "
    + "by using the + operator"
    + " "
    + "on strings"
)

print('hello' * 3) # for repetition strings


# STRING FORMATTING
# f-strings: the most common and simplest way to format strings
# embed variables or expressions in string
print(f'The sum of 3 and 5 is {3 + 5}')

# format: use {} from placeholders, pass values positionally
print('I am the {}, i teach {}, and i love to be in {}'.format('instructor', 'python', 'new horizons'));


# Membership TESTING
print('not' in 'string is not complex')

# LAMBDA FUNCTION
"""This is anonymous function in python, means the function does not have a name"""

summation = lambda a, b: a + b
print(summation(3, 2))

posNeg = lambda num: "positive" if num > 0 else "negative" if num < 0 else "zero"
print(posNeg(5))
print(posNeg(0))
print(posNeg(-11))


# USING FOR LIST COMPREHENSION
li = [(lambda arg=x: arg * 2)() for x in range(5)]
# for i in li:
#     print(i)


# # USING FOR RETURN MULTIPLE RESULTS
calc = lambda x, y: (x - y, x * y);
print(calc(2, 3));


# USING WITH FILTER
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even = filter(lambda x: x % 2 is 0, arr);
print(list(even))

# USING MAP
a = [2, 4, 5];
b = map(lambda x: x * 2, a);
print(list(b))
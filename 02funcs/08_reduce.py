'''reduce function applies a function cumulatively to an iterable, reducing it to a single value'''

from functools import reduce;
li = ['Geeks', 'for', 'Geeks'];
print(reduce(lambda x, y: x + " " + y, li))

li = [1, 2, 3, 4];
print(reduce(lambda x, y: x + y, li))

def add(x, y):
    return x + y;
a = [1, 2, 3, 4, 5, 6];
print(reduce(add, a));
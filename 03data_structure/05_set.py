set1 = {1, 2, 3, 4, 5}
set2 = set()

"""we can create a new set fro other data type
"""

print(set1)

try:
    print(set1[0])
except TypeError:
    print(TypeError)


set1 = {1, 2, 3}
set1.add(4)

print(set1)

set1.update([3, 4, 5, 6, 7, 8, 9, 10])
print(set1)
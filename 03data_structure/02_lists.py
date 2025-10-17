"""Lists is a data structure in python, that can hold an ordered collection of items
It is mutable, it can store mixed data types and also index based"""

# CREATING A LIST
lst = []  # using square brackets
lst2 = list(("name", "age", "personality"))  # using the list constructor function
print(type(lst), type(lst2))


listInt = [1, 2, 3, 4, 5]
# list of ints
listStr = ["apple", "banana", "cherry"]
# list of strings
listMixed = [1, "apple", 22, "banana", 3, "cherry"]


# Creating list with repeated value
a = [2] * 3  # [2, 2, 2]


# Accessing items in list
"""Just like strings, it is done using index, positive indices and negative indices"""
print(listMixed[0])
print(listMixed[1:4])
print(listMixed[-1:-4])  # empty array, cas no item on the right of -1 index
print(listMixed[-4:-1])
print(listMixed[::-1])  # reverse list
print(listMixed)


# MANIPULATING LIST (MUTATING LIST)
lst = [1, "boy"]
lst.append(10)  # for adding a single item
print(lst)

lst.extend([1, 20, "girl", "jose", "maria"])  # adding multiple items
print(lst)

lst.insert(0, 20)  # add to a specific position - in indexPosition 0 add 20
print(lst)

# lst.clear() # to remove every item in a list
# print(lst)

# updating
lst[0] = 20
print(lst)

# deleting an item
lst.remove("girl")
# finds 'girl' in the list and removes it without holding the value
print(lst)

popped = lst.pop(2)
# removes item at a specific index and holds the value;
print(lst)
print(popped)

del lst[5]
# removes item at a specific index too
print(lst)

# ITERATING OVER A LIST
for item in lst:
    print(item)

# NESTED LIST
nestedLst = [[1, 2, 4, ["boy", "girl", ["man", "woman"]]]]
print(nestedLst)


# LIST COMPREHENSION
lst = [x**2 for x in range(5)]
print(lst)
lst.reverse();
print(lst)
lst2 = [""]
# LOOPS
"""Loops are used to repeat actions efficiently"""

# FoR Loop - counting through items, used to iterate over a sequence
# range(start, stop, skip);
for x in range(6):
    print(x)

list1 = [1, 2, 3, 4]
for x in list1:
    print(x)

tup1 = ("one", "tue", "me")
for x in range(len(tup1)):
    print(tup1[x], end=" ")
else:
    print("\n Inside else block")

iterator = 0
while iterator < 5:
    print(iterator, end="^")
    iterator += 1
print()

# Nested loop both for and while

# loop control statement
for letter in "JOsemaria":
    if letter.lower() == "j" or letter.lower() == "r":
        continue  # continue to skip to next iteration, break to break out of loop
    print(letter)

# pass
"""pass is used for empty control statement, function, class, method"""
for x in "jose":
    pass
print(x)
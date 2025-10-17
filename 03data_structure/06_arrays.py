# import array as arr;
from array import *

a = array('i', [1, 2, 3]);
print(*a, a);

try:
    b = array('s', [1, 2, 4])
except  ValueError as v:
    print(v)
print(b)
b.reverse();
print(b)
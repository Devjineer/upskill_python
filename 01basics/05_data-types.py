from log import log;
# DATA TYPES
'''
- numbers - int, float, complex
- dictionary
- boolean
- set
- sequence - tuple, list, string
'''
list1 = [1, 2, 3]; # list is collection of data, arranged in an orderly manner
tpl1 = (1, 2, 3); # same with list just immutable

dict1 = {
    1: 'jose',
    2: 'name',
    'name': "Josemaria"
}

log(dict1.get(1), dict1['name'], dict1[1]); # NOTE: accessing a variable
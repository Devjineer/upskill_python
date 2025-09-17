age = 18

if age >= 18:
    print("Eligible to vote")

age = 10

if age <= 12:
    print("Travel for free")
else:
    print("Pay for Ticket")


# elif
# nested if
# ternary

# match case is the switch for python
day = int(input('input a day in number and i will tell what day it is:'));

match day:
    case 1:
        print('Monday');
    case 2 | 3:
        print('Tues Weds');
    case _:
        print('Other number')

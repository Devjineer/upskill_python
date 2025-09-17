print("Welcome to python calculator!!!")
done = False
numOfCalcDone = 0


def calculator():

    num1 = float(input("Please add your first number: "))

    operator = input("what operation you want to do? *, +, -, / ")
    while operator not in ["*", "+", "-", "/"]:
        print("Invalid Operator")
        operator = input("what operation you want to do? *, +, -, / ")

    num2 = float(input("Please add your second number: "))

    while operator == "/" and num2 == 0:
        print("Please input a digit that is not 0")
        num2 = float(input("Please add your second number"))

    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num2 * num1
    elif operator == "/":
        result = num1 / num2
    else:
        result = num1 - num2
    # numOfCalcDone += 1;
    print(f"{num1} {operator} {num2} is {result}")


while not done:
    numOfCalcDone += 1
    calculator()
    done = (
        True
        if str(input("Do you want to continue? (Yes/No)")).lower() == "no"
        else False
    )
else:
    print(
        f"Thanks for using the calculator! You completed {numOfCalcDone} calculations 🎉"
    )
"""
TODO: LATER ON
Adding more operators → %, **, //.
Keeping history → store results in a list and show them at the end.
Handling invalid number inputs → wrap float(input(...)) in a try/except.
Modular design → split input, validation, and calculation into separate functions.
"""

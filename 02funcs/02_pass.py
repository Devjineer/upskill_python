"""pass is a keyword that acts as a placeholder where a statement is needed but we do nothing
Because keeping code blocks empty will throw an error"""

if True:
    pass


def func():
    pass


func()

x = 10
if x > 5:
    pass
else:
    print("x is 5 or less")

for i in range(6):
    if i == 3:
        pass
    else:
        print(i);
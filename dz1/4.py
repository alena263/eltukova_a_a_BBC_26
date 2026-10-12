import math
a = input()
if a in ("sqrt", "sin", "cos", "tan", "log", "+", "-", "/", "*"):
    x = int(input())
    if a in ("+", "-", "/", "*"):
        y = int(input())
    if a == "sqrt":
        if x < 0:
            print("Ошибка")
        else:
            print(math.sqrt(x))
    elif a == "sin":
        print(math.sin(math.radians(x)))
    elif a == "cos":
        print(math.cos(math.radians(x)))
    elif a == "tan":
        print(math.tan(math.radians(x)))
    elif a == "log":
        print(math.log(x))
    elif a == "+":
        print(x + y)
    elif a == "-":
        print(x - y)
    elif a == "*":
        print(x * y)
    elif a == "/":
        if y == 0:
            print("Ошибка")
        else:
            print(x / y)
else:
    print("Неверная операция")
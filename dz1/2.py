def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def umn(x, y):
    return x * y
def dell(x, y):
    return x / y
b = int(input())
a = input()
c = int(input())
if a == "+":
    print(plus(b, c))
if a == "-":
    print(minus(b, c))
if a == "*":
    print(umn(b, c))
if a == "/":
    print(dell(b, c))
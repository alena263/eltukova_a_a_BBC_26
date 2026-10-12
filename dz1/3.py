def f(x, y, z):
    if x == "+":
        return y + z
    elif x == "-":
        return y - z
    elif x == "/":
        return y / z
    elif x == "*":
        return y * z
while True:
    b = int(input())
    a = input()
    c = int(input())
    print(f(a, b, c))
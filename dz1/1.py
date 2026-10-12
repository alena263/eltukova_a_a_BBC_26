b = int(input())
a = input()
c = int(input())
if a == "+":
    res = b + c
elif a == "-" and b >= c:
    res = b - c
elif a == "/":
    res = b / c
elif a == "*":
    res = b * c
print(res)
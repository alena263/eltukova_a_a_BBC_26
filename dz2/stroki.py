def lvl1(a):
    print('1 - преобразовать все символы в верхний регистр')
    print('2 - преобразовать все символы в строчный регистр')
    print('3 - делает все адекватным')
    a = int(input('Выберите метод: '))
    test_1 = str(input('Введите строку '))
    if a == 1:
        print(test_1.upper())
    if a == 2:
        print(test_1.lower())
    if a == 3:
        print(test_1.capitalize())
def lvl2():
    print('1 - найти 1-ое вхождение слова/символа')
    print('2 - заменить любое слово на другое')
    print('3 - посчитать любой символ')
    a = int(input('Выберите метод: '))
    test_2 = str(input('Введите строку: '))
    if a == 1:
        b = str(input('Введите слово или символ: '))
        return test_2.find(b)
    if a == 2:
        b = str(input('Введите слово, которое хотите заменить: '))
        q = str(input('На какое? '))
        return test_2.replace(b, q)
    if a == 3:
        b = str(input('Какой символ посчитать? '))
        return test_2.count(b)
def lvl3():
    s = str(input('Введите строку с которой хотите работать: '))
    a = str(input('Какой разделитель? '))
    b = str(input('Как соединить? '))
    s = s.split(a)
    res = b.join(s)
    return res

def lvl4():
    s = str(input('Введите строку которую хотите сделать крутой '))
    n = int(input('Введите 1 если хотите оставить цифры, 2 если числа, 3 и то и другое '))
    s = s.strip()
    s = list(s)
    for i in range(len(s)):
        if n == 1:
            if s[i].isdigit():
                continue
            else:
                s[i] = ''
        if n == 2:
            if s[i].isalpha():
                continue
            else:
                s[i] = ''
        if n == 3:
            if (s[i].isalpha() or s[i].isdigit()):
                continue
            else:
                s[i] = ''
    s = ''.join(s)
    res = 'Вот ваша строка: {}'.format(s)
    return res

def lvl5():
    s = str(input('Введите сумасшедшую строку '))
    s = s.strip()
    s = list(s)
    for i in range(len(s)):
        if not (s[i].isalpha() or s[i] == ' '):
            s[i]=''
    s = ''.join(s)
    s = s.capitalize()
    return s

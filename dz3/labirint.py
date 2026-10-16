import random

size = 5
types = ["пусто", "сундук", "монстр", "ловушка", "портал"]
loot = ["золото", "зелье", "меч", "щит"]

icons = {
    "пусто": ".",
    "сундук": "C",
    "монстр": "M",
    "ловушка": "!",
    "портал": "O",
    "ключ": "K",
    "старт": "S",
    "выход": "E"
}

rooms = []
visited = []
inv = []

hp = 100
x = 0
y = 0

# Создание лабиринта
for i in range(size):
    row = []
    vis = []

    for j in range(size):
        row.append(random.choice(types))
        vis.append(False)

    rooms.append(row)
    visited.append(vis)

rooms[0][0] = "старт"
rooms[4][4] = "выход"

# Размещение ключа
while True:
    i = random.randint(0, 4)
    j = random.randint(0, 4)

    if rooms[i][j] != "старт" and rooms[i][j] != "выход":
        rooms[i][j] = "ключ"
        break


# Использование зелья
def potion(hp):
    if "зелье" in inv:
        inv.remove("зелье")
        hp = min(100, hp + 30)
        print("Вы выпили зелье. HP:", hp)
    else:
        print("У вас нет зелья!")

    return hp


# Бой с монстром
def fight(hp):
    monster = random.randint(20, 35)

    while monster > 0 and hp > 0:
        print("Монстр:", monster, "HP. Вы:", hp, "HP")
        a = input("1 — ударить, 2 — зелье, 3 — бежать: ")

        if a == "1":
            damage = random.randint(5, 15)

            if "меч" in inv:
                damage += 5

            monster -= damage
            print("Вы нанесли урон:", damage)

        elif a == "2":
            hp = potion(hp)

        elif a == "3":
            if random.random() < 0.5:
                print("Вы сбежали!")
                return hp
            else:
                print("Сбежать не удалось!")

        else:
            print("Неизвестная команда")
            continue

        if monster > 0:
            damage = random.randint(5, 12)

            if "щит" in inv:
                damage //= 2

            hp -= damage
            print("Монстр нанёс урон:", damage)

    if hp > 0:
        inv.append("золото")
        print("Монстр побеждён! Вы получили золото.")

    return hp


# Основная часть игры
while hp > 0:

    # Проверка комнаты
    if not visited[x][y]:
        visited[x][y] = True
        room = rooms[x][y]

        print("Вы вошли в комнату:", room)

        if room == "сундук":
            item = random.choice(loot)
            inv.append(item)
            print("Вы нашли:", item)

        elif room == "ключ":
            inv.append("ключ")
            print("Вы нашли ключ!")

        elif room == "ловушка":
            damage = random.randint(10, 25)

            if "щит" in inv:
                damage //= 2

            hp -= damage
            print("Ловушка! Получен урон:", damage)

        elif room == "монстр":
            hp = fight(hp)

        elif room == "портал":
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            print("Портал перенёс вас в другую комнату!")
            continue

    if hp <= 0:
        break

    # Вывод карты
    for i in range(size):
        line = []

        for j in range(size):
            if i == x and j == y:
                line.append("@")
            elif visited[i][j]:
                line.append(icons[rooms[i][j]])
            else:
                line.append("?")

        print(" ".join(line))

    print("HP:", hp)

    # Проверка победы
    if x == 4 and y == 4:
        if "ключ" in inv:
            print("Вы открыли выход. Победа!")
            break
        else:
            print("Выход закрыт. Найдите ключ!")

    command = input("w/a/s/d — идти, i — инвентарь, q — выйти: ").lower()

    # Инвентарь
    if command == "i":
        while True:
            print("Инвентарь:", inv)
            a = input("1 — сортировать, 2 — зелье, 0 — назад: ")

            if a == "1":
                inv.sort()
            elif a == "2":
                hp = potion(hp)
            elif a == "0":
                break
            else:
                print("Неизвестная команда")

    elif command == "q":
        break

    # Передвижение
    elif command == "w":
        if x > 0:
            x -= 1
        else:
            print("Там стена!")

    elif command == "s":
        if x < 4:
            x += 1
        else:
            print("Там стена!")

    elif command == "a":
        if y > 0:
            y -= 1
        else:
            print("Там стена!")

    elif command == "d":
        if y < 4:
            y += 1
        else:
            print("Там стена!")

    else:
        print("Неизвестная команда")

if hp <= 0:
    print("Ваше здоровье закончилось. Вы проиграли!")
import pandas as pd
import numpy as np

df = pd.read_csv("tested.csv") ## считывание данных из csv файла
size_before = df.shape
## print(df) ## проверка, что данные верно выгрузились

## (пункт 7) вывод n строк таблицы
'''
n = int(input("Введите количество строк: "))
print(df.head(n))
'''

## print(df.tail(5)) ## вывод последних 5 строк таблицы (пункт 8)

## (пункт 9) shape - хранит  в себе размеры таблицы [418, 12]
'''
print("Количество строк: ", df.shape[0])
print("Количество столбцов: ", df.shape[1])
'''

## print(df.columns) ## содержит в себе названия всех столбцов таблицы (пункт 10)

## print(df.dtypes) ## пункт 11

## пункт 12
numbers = ['Age', 'SibSp', 'Parch', 'Fare']
categories = ['PassengerId', 'Survived', 'Pclass', 'Name',\
              'Sex', 'Ticket', 'Cabin', 'Embarked']
print(numbers, categories)

## пункт 13. Статистические показатели
'''
for a in numbers:
    print(a)
    print("Среднее: ", df[a].mean())
    print("Медиана: ", df[a].median())
    print("Минимум: ", df[a].min())
    print("Максимум: ", df[a].max())
    print("Стандартное отклонение: ", df[a].std())
'''
'''
## 14. Количество пассажиров каждого класса
print(df["Pclass"].value_counts())
'''
'''
## 15. Количество уникальных портов
print(df["Embarked"].nunique())
'''
## 16. Количество пропусков
missing = df.isna().sum()
print(missing)

## 17. Процент пропусков от общего числа строк
procent = (missing/df.shape[0])*100
print(procent)

## 18. Столбец с макс колвом пропусков
print(missing.idxmax())

## 19. Статистика возраста до заполнения
before = [
    df["Age"].mean(),
    df["Age"].median(),
    df["Age"].min(),
    df["Age"].max(),
    df["Age"].std(),
    df["Age"].count()
]
print(before)

## 20. Заполнение пропусков медианой
median = before[1]
df["Age"] = df["Age"].fillna(median)

## 21. Статистика возраста после заполнения
after = [
    df["Age"].mean(),
    df["Age"].median(),
    df["Age"].min(),
    df["Age"].max(),
    df["Age"].std(),
    df["Age"].count()
]
print(after)

## 22. Сравнение до и после заполнения
comparison = pd.DataFrame({
    "Показатель": [
        "Среднее арифметическое",
        "Медиана",
        "Минимальный возраст",
        "Максимальный возраст",
        "Стандартное отклонение",
        "Количество известных значений"
    ],
    "До обработки": before,
    "После обработки": after
})
print(comparison)

## 23. Удаление строк без порта посадки
df = df.dropna(subset=["Embarked"])

## 24. Удаление столбца Cabin
print(procent["Cabin"])
if procent["Cabin"] > 50:
    df = df.drop(columns=["Cabin"])
    print("Столбец Cabin удалён")
else:
    print("Столбец Cabin не удалён")

## 25. Оставшиеся пропуски
print(df.isna().sum())

## 26. Кол-во строк и столбцов до обработки и после обработки
print("Размер таблицы до обработки: ",size_before)
print("Размер таблицы после обработки: ", df.shape)

##
age = df["Age"].to_numpy()
sex = df["Sex"].to_numpy()
survived = df["Survived"].to_numpy()
fare = df["Fare"].to_numpy()

## 31. Общий процент выживших
print(np.mean(survived) * 100)

## 32. Процент выживших мужчин и женщин
print("Мужчины:", np.mean(survived[sex == "male"]) * 100)
print("Женщины:", np.mean(survived[sex == "female"]) * 100)

## 33. Средний возраст мужчин и женщин
print("Мужчины:", np.mean(age[sex == "male"]))
print("Женщины:", np.mean(age[sex == "female"]))

## 34. Средний возраст выживших и погибших отдельно
## для мужчин и для женщин
print("Выжившие мужчины: ",
      np.mean(age[(sex == "male") & (survived == 1)]))
print("Погибшие мужчины: ",
      np.mean(age[(sex == "male") & (survived == 0)]))
print("Выжившие женщины: ",
      np.mean(age[(sex == "female") & (survived == 1)]))
print("Погибшие женщины: ",
      np.mean(age[(sex == "female") & (survived == 0)]))

## 35. Стоимость билетов
print("Минимум: ", np.nanmin(fare))
print("Максимум: ", np.nanmax(fare))
print("Среднее: ", np.nanmean(fare))

## 36. Стандратное отклонение возраста
print(np.std(age))

## Результаты сравнительного анализа
result = pd.DataFrame({
    "Пол": ["Мужчины", "Женщины"],

    "Процент выживших": [
        np.mean(survived[sex == "male"]) * 100,
        np.mean(survived[sex == "female"]) * 100
    ],

    "Средний возраст": [
        np.mean(age[sex == "male"]),
        np.mean(age[sex == "female"])
    ],

    "Возраст выживших": [
        np.mean(age[(sex == "male") & (survived == 1)]),
        np.mean(age[(sex == "female") & (survived == 1)])
    ],

    "Возраст погибших": [
        np.mean(age[(sex == "male") & (survived == 0)]),
        np.mean(age[(sex == "female") & (survived == 0)])
    ]
})

print(result.to_string())

## Часть V. Фильтрация данных
## Задание 1
res1 = df[
    (df["Sex"] == "male") &
    (df["Age"] > 30) &
    (df["Pclass"] == 1)
]
print("Количество пассажиров: ", res1.shape[0])
print(res1.head(10))
## Задание 2
res2 = df[
    ((df["Age"] < 18) |
    (df["Sex"] == "female")) &
    (df["Survived"] == 1)
]
print("Количество пассажиров: ", res2.shape[0])

## Задание 3
third = df[df["Pclass"] == 3]
average = third["Fare"].mean()
res3 = third[third["Fare"] > average]
print(res3)

## Задание 4
twentyto40 = df[(df["Age"] >= 20) & (df["Age"] <= 40)]
res4 = twentyto40[twentyto40["Embarked"] == "S"]
print(res4)

## 37. Группировка по классу и полу
statistics = df.groupby(["Pclass", "Sex"]).agg({
    "PassengerId": "count",
    "Age": "mean",
    "Survived": "mean",
    "Fare": "mean"
})
statistics["Survived"] = statistics["Survived"] * 100
print(statistics)

## 38. Группировка по порту посадки
port = df.groupby(["Embarked"]).agg({
    "PassengerId": "count",
    "Survived": "mean",
})
port["Survived"] = port["Survived"] * 100
print(port)

## 39. Класс пассажиров с наибольшей долей выживших
clas = df.groupby("Pclass")["Survived"].mean() * 100
otv = clas.idxmax()
print(clas)
print(otv)

## Часть VII. Сохранение результатов
## 40. Сохранение обработанной таблицы
df.to_csv("titanic_processed.csv", index=False)
print("Обработанная таблица сохранена")

## 41. Сохранение статистики
statistics = statistics.reset_index()
statistics.to_csv("titanic_statistics.csv", index=False)
print("Статистика сохранена")

## 42. Проверка сохраненных данных
check = pd.read_csv("titanic_processed.csv")
pd.testing.assert_frame_equal(
    df.reset_index(drop=True),
    check,
    check_exact=False
)
print("Данные сохранены правильно")
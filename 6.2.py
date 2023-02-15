import random as r

x = [
    "Алим",
    "Мансур",
    "Фарида",
    "Роман",
    "Николай",
    "Александр",
    "Михаил",
    "Алексей",
    "Сергей",
    "Владимир",
    "Пётр",
    "Георгий",
    "Дмитрий",
    "Мария",
    "Анна",
    "Екатерина",
    "Клавдия",
    "Татьяна",
    "Вера",
    "Елизавета",
    "Ольга",
    "Елена",
    "Владимир",
    "Виктор",
    "Юрий",
    "Борис",
    "Евгений",
    "Валентин",
    "Валентина",
    "Нина",
    "Лидия",
    "Людмила",
    "Надежда",
    "Андрей",
    "Денис",
    "Павел",
    "Игорь",
    "Илья",
    "Наталья",
    "Юлия",
    "Мария",
    "Светлана",
    "Владислав",
    "Богдан",
    "Алеся",
    "Ростислав",
    "Кристина",
    "Людмила",
    "Майя",
    "Анфим",
    "Марта",
    "Оксана",
    "Виталий",
    "Милана",
    "Трофим",
    "Ярослав",
    "Серафим",
    "Олег",
    "Юрий",
    "Руслан",
]
h1 = set(r.choices(x, k=20))
while len(h1) < 20:
    h1.add(r.choice(x))
h2 = set(r.choices(x, k=20))
while len(h2) < 20:
    h2.add(r.choice(x))
h3 = set(r.choices(x, k=20))
while len(h3) < 20:
    h3.add(r.choice(x))
print("Списки групп:")
print(f"Первая группа ({len(h1)} человек):", *h1)
print(f"Вторая группа ({len(h2)} человек):", *h2)
print(f"Третья группа ({len(h3)} человек):", *h3)
print()
t = h1.intersection(h2, h3)
onlyOne = h1.difference(h2, h3)
onlyOne.update(h2.difference(h1, h3))
onlyOne.update(h3.difference(h2, h3))
print("Список тезок:", *t, sep="\n")
print()
print("Нет тезок в других группах:", *onlyOne, sep="\n")

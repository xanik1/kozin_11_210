from random import randint


count = 0
corr = 0
numbers = []
print('Какое число от 0 до 9 загадано сейчас (q - закончить)?')
n = input()
while n != 'q':
    if 0 <= int(n) <= 9:
        x = randint(0, 9)
        if int(n) == x:
            corr += 1
            count += 1
            numbers.append(x)
        else:
            count += 1
            numbers.append(x)
    else:
        print('Введите другое число')
    print('Статистика (угадано/не угадано):', round((corr / count) * 100), '%', '/', round(100 - (corr / count * 100)), '%')
    print('Загаданные числа:', numbers)
    print('Какое число от 0 до 9 загадано сейчас (q - закончить)?')
    n = input()

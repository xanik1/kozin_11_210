x = float(input())
y = float(input())
n = int(input())
if n > x and n > y:
    print('Попадает')
else:
    if n < x and n < y:
        print('Не попадает')
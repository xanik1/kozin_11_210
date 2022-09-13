import math
x = float(input())
y = float(input())
n = int(input())
h = math.sqrt(x ** 2 + y ** 2)
if h <= n:
    print('Попадает')
else:
    print('Не попадает')
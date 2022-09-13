x = float(input())
y = float(input())
m = 11
for i in range(1, 11):
    if ((x ** 2 + y ** 2) ** 0.5) < i:
        if i < m:
            m, i = i, m
if m == 11:
    print('missed')
else:
    print(m)

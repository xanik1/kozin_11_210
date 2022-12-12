a = input().split()
b = int(input())


x = 0
y = len(a) - 1
m = (x + y) // 2


while b != int(a[m]):
    if b > int(a[m]):
        x = m + 1
    else:
        y = m - 1
    m = (x + y) // 2


print(m)
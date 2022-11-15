n = input().split()
a = ['1']
k = 1
for i in n:
    if int(i) > 0:
        a.append(i)
    else:
        continue
for j in a:
    if len(a) == 1:
        quit()
    else:
        k *= int(j)
print(k)
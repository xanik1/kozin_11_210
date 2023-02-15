h = int(input())
x = []
for i in range(h):
    s = input()
    count = 0
    k = s.find("1")
    while k < len(s):
        t = s.find("1", k + 1)
        if t > -1:
            count += t - k - 1
            k = t
        else:
            k += 1
    x.append(count)
for i in range(len(x)):
    print(x[i])
def compress(x):
    r = ""
    a = 0
    while a < len(x):
        count = 1
        r += x[a]
        while a < len(x) - 1 and x[a] == x[a + 1]:
            count += 1
            a += 1
        if count > 1:
            r += str(count)
        a += 1
    return r


x = input()
while x != "quit":
    print(compress(x))
    x = input()

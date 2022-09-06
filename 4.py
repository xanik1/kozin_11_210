count = {}
n = input()
x = n.lower()
for i in x:
    if i.isalpha():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
print(count)


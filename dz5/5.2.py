def find_nick(a, s):
    for i in range(len(a)):
        if a[i][0] == s:
            return find_nick(a, a[i][1])
    return s

x = int(input())
a, res, ans = [], [], []
repeat = False
for i in range(x):
    a.append(input().split())
for i in range(len(a)):
    res.append([a[i][0], find_nick(a, a[i][1])])
for i in range(len(res)):
    for j in range(i + 1, len(res) - 1):
        if res[i][1] == res[j][1]:
            res.pop(j)
print(len(res))
for i in range(len(res)):
    print(*res[i])
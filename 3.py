x = input().split()
n = int(input())
for i in x:
    if int(i) == n:
        print(x.index(i))
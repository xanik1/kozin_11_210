n = int(input())
k = 1
count = 0
while k <= n:
    count = count + (n ** k)
    k += 1
print(count)
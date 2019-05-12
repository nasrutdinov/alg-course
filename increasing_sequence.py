a = []
f = ("file.txt")
for line in f:
    a += list(map(int, line.split()))

print(a)

n = len(a)
d = [1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j] and d[i]<d[j]+1:
            d[i] = d[j] + 1
            print()

print(d)
l = d.index(max(d))

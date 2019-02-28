x = y = 1
for i in range(20):
    x, y = y, x + y
    print(x)


def f(x):
    if (x == 0) or (x == 1):
        return x
    t = f(x - 1) + f(x - 2)
    return (t)


print(f(20))

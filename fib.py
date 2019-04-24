import time

start1 = time.time()
x = y = 1
for i in range(19):
    x, y = y, x + y
end1 = time.time()
print('first: ',x,'time: ',end1 - start1)

start2 = time.time()
def f(x):
    if (x == 0) or (x == 1):
        return x
    t = f(x - 1) + f(x - 2)
    return (t)
end2 = time.time()

print('Second: ',f(20),'time: ',end2 - start2)

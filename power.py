import time

def fast_power(x, n):
    '''Быстрое возведение в степень числа'''
    def even(n):
        if n%2==0:
            return 1
        return 0
    if n==0:
        return 1
    if even(n):
        return fast_power(x, n/2)**2
    return x*fast_power(x, n-1)

def slow_power(x, y):
    number = 1
    while y:
        if y & 1:
            number = number * x
        y >>= 1
        x = x * x
    return number

start1 = time.time()
print(fast_power(3,10))
end1 = time.time()
print('fast_power: ',end1 - start1)

start2 = time.time()
print(slow_power(3,10))
end2 = time.time()
print('other_fast_power: ',end2 - start2)

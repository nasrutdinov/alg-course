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

def slow_power(x, n):
    '''Долгое возведение в степень'''
    def even(n):
        if n%2==0:
            return 1
        return 0
    a=1
    if not even(n):
        a=x
        n-=1
    while n!=1:
        x*=x
        n/=2
    x*=a
    return x

start1 = time.time()
print(fast_power(3,11))
end1 = time.time()
print('fast_power: ',end1 - start1)

start2 = time.time()
print(slow_power(3,7))
end2 = time.time()
print('other_fast_power: ',end2 - start2)

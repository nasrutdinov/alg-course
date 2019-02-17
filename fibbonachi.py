def fib(n):
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)

for n in range(38):
    print("n=", n, " fib=", fib(n))

f0=1
f1=1

for n in range(2,38):
    f0,f1=f1,f0+f1
    print("n=", n, " fib=", f1)
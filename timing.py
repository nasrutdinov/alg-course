import time
#подключение библиотеки для графики
from  matplotlib import pyplot as plt

def timed(f, *args, n_iter=100):
    acc = float("inf")
    #засекаем время начала программы
    t0 = time.perf_counter()
    #для подсчета быстрых процессов приходится запустить один и тот же процесс n_iter раз
    for i in range(n_iter):
        f(*args)
    #время исполнения
    acc = min(acc, time.perf_counter() - t0)        
    return acc

#функция отрисовки времени исполнения разных программ
def compare(fs, args):
    xs = list(range(len(args)))
    for f in fs:
        plt.plot(xs, [timed(f, chunk) for chunk in args],
                 label=f.__name__)
    plt.legend()
plt.grid(True)

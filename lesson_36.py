# from time import perf_counter
#
#
# class T:
#     def __init__(self, f):
#         print('Class __init__ is running')
#         self.f = f
#
#     def __call__(self, *args, **kwargs):
#         print(f'Method __call__ is running,\n'
#               f'calculating function {self.f.__name__} and args {args}')
#         start = perf_counter()
#         res = self.f(*args, *kwargs)
#         end = perf_counter()
#         print(f'Running time is {round(end - start, 5)}')
#         return res
#
#
# def factorial(x):
#     pr = 1
#     for i in range(1, x + 1):
#         pr *= i
#     return pr
#
#
# def fib(x):
#     if x <= 2:
#         return 1
#     return fib(x - 1) + fib(x - 2)
#
# _____________________________
#
# import time
#
#
# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args):
#         start = time.time()
#         result = self.fn(*args)
#         finish = time.time()
#         print(f'Отработала за {finish - start}')
#
#
# _________________________________
#
from time import perf_counter
class Timer:

    def __init__(self, func):
        self.func = func


    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f'Время работы программы {finish-start}')
        return result
@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()
#
# class Addition:
#
#     def __call__(self, *args, **kwargs):
#         count = 0
#         for i in args:
#             if isinstance(i,(int,float)):
#                 count += i
#         print(f'Сумма переданных значений = {count}')
#
# add = Addition()
#
# add(10, 20) # печатает "Сумма переданных значений = 30"
# add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
# add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"

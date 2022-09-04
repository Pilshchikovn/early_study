def say_name(name):
    def say_goodbye():
        print(f'Don\'t say me goodbye\n{name}!')

    return say_goodbye


f = say_name('Misha')
f2 = say_name('Oleg')
f()
f2()

def counter(start=0):
    def step():
        nonlocal start
        start +=1
        return start
    return step

x = counter(5)
x1 = counter()
print(x(), x1())
print(x(), x1())
print(x(), x1())

def func_decorator(funk):
    def wrapper(*args, **kwargs):
        print('do smth before')
        funk(*args, **kwargs)
        print('do smth after')

    return wrapper


def some_func(title):
    print(f'title = {title}')

some_func = func_decorator(some_func)
some_func('Hello world')

def func_decorator(funk):
    def wrapper(x, *args, **kwargs):
        dx = 0.00001

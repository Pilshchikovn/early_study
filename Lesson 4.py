import time


def get_nod(a, b):
    ''' Вычисляется НОД по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    '''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod(func):
    # --- test №1 ---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test 1 passed')
    else:
        print('test 1 failed')
    # --- test №2 ---
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test 2 passed')
    else:
        print('test 2 failed')
    # --- test №3 ---
    a = 10000000
    b = 2
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print(dt, 'test 3 passed')
    else:
        print(dt, 'test 3 failed')


test_nod(get_nod)


def quick_get_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


print(quick_get_nod(10000000000000, 2))

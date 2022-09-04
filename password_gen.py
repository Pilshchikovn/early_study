# from string import *
# from random import *
#
# LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
#
# def generate_password(m):
#     return ([choice(LETTER) for _ in range(m)])
#
# def generate_passwords(n, m):
#     for i in range(n):
#         print(*generate_password(m),sep='')
#
# n, m = int(input('Введите количество паролей: ')), int(input('Введите длинну пароля: '))
# generate_password(m)
# generate_passwords(n, m)

import string
import random


# def generate_password(length):
#     s = ''.join([i for i in (string.printable[:62]) if i not in '10OolI'])
#     return (''.join(random.sample(s[:8], 1) + random.sample(s[8:30], 1) + random.sample(s[30:], length - 2)))
#
#
# def generate_passwords(count):
#     return [generate_password(m) for _ in range(count)]
#
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n), sep='\n')

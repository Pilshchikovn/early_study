# import random
#
# n = int(input())    # количество попыток
# for i in range(n):
#     print(random.choice(['Орел','Решка']))

# import random
#
# chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# length = int(input())  # длина пароля
# password = []
# for i in range(length):
#     print(random.choice(chars),end='')
#
# from random import *
#
# for _ in range(int(input())):
#     print(chr(choice([randint(65, 90), randint(97, 122)])), end='')

# import random
# print(*sorted([random.randint(1,49) for x in range(7)]))


# from random import randrange as r
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'
# print(generate_ip())


# from random import *
# import string
# def generate_index():
#     return f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{randrange(100)}_{randrange(100)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
#
# print(generate_index())

# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for i in range(len(matrix)):
#     random.shuffle(matrix[i])
# print(matrix)

# from random import randint
# s=set()
# while len(s)!=100:
#     s.add(randint(1000000,9999999))
# print(*s,sep='\n')

# import random
# l = [input() for _ in range(int(input()))]
# print(l)
# random.shuffle(l)
# print(l)
# for i in range(len(l)):
#     print(f'{l[i-1]} - {l[i]}')
#

from string import *
from random import *

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(m):
    return ([choice(LETTER) for _ in range(m)])

def generate_passwords(n, m):
    for i in range(n):
        print(*generate_password(m),sep='')

n, m = int(input('Введите количество паролей: ')), int(input('Введите длинну пароля: '))
generate_password(m)
generate_passwords(n, m)

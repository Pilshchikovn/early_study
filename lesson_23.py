# numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
# print(numbers)

# numbers = ((0, (9, 2)), (1, (4, 6, 3), (5, 2, 3), 8, 3))
# print(numbers[0][1][1])

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if i!=()]
#
# print(non_empty_tuples)

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in range(len(numbers)):
#     print(numbers[i])
#
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for num in numbers:
#     print(num)

# letters = 'abcdefghijkl'
# tpl = (letters,)
# print(tpl)

# number = 12345
# tpl = (number,)
# print(tpl)
# print(type(tpl))


# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# s= list(poet_data)
# s[2]='Москва'
# print(tuple(s))
#
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:-1] + ('Москва',)
#
# print(poet_data)
# 1
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# s=list(numbers)
# k=[]
# for i in s:
#     k.append(sum(i)/len(i))
# print(k)
# 2
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# print([sum(i) / len(i) for i in numbers])


# a,b,c = int(input()),int(input()),int(input())
# y=(a*x)**2 + b*x + c
# print(tuple(-(b/(2*a)), ((4*a*c) - (b**2))/(4*a)))
#
# def coords(a, b, c):
#     x = -(b / (2 * a))
#     y = (4 * a * c - b**2) / (4 * a)
#     return x, y
#
# result = coords(int(input()), int(input()), int(input()))
# print(result)

# s = [input().split() for i in range(int(input()))]
# for i in range(len(s)):
#     print(s[i][0], s[i][1])
# print()
# for i in range(len(s)):
#     if s[i][1] in '45':
#         print(s[i][0], s[i][1])

# s=[input().split() for i in range(int(input()))]
# for i in range(len(s)):
#     print(s[i][0],s[i][1])
# print()
# for i in range(len(s)):
#     if s[i][1] in '45':
#         print(s[i][0],s[i][1])
#
# myset1 = set(range(10))          # множество из элементов последовательности
# myset2 = set([1, 2, 3, 4, 5])    # множество из элементов списка
# myset3 = set('abcd')             # множество из элементов строки
# myset4 = set((10, 20, 30, 40))
# print((myset3))

# myset = set(['ъъъ', 'эээ', 'ююю', 'яяя'])
# print(myset)

# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# sorted_numbers = sorted(numbers)
# print(*sorted_numbers, sep='\n')

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum([i**2 for i in numbers]))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# print(*sorted(fruits, reverse=True),sep='\n')

# print(len(set(input())))

# n = input()
# print('YES' if len(n) == len(set(n)) else 'NO')
#
# n,m=input(),input()
# if len(set(n+m)) ==10:
#     print('YES')
# else:
#     print('NO')

# or Там все просто на самом деле. Кортеж с двумя вариантами ответов,
# в квадратных скобках получится индекс одного из вариантов,
# потому что логические тру и фолс эквивалентны единичке и нулю соответственно.
# print(('NO', 'YES')[len(set(input() + input())) == 10])
# Ты смотри на индексы в этом кортеже. У No - 0, у Yes - 1.
# Индексы тут - булевы значения No и Yes, улавливаешь?

# n,m,k=input().split()
# if set(n) ==set(m)==set(k):
#     print('YES')
# else:
#     print('NO')
#


# numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
# res = 0
#
# for num in numbers:
#     res += (num % 2 == 0)
# print(res)
#
# if flag == True:
# if flag:
#
# if flag == False:
# if not flag:
#
# not and or


# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)

# def is_even(num):
#     return num % 2 == 0
#
#
# def func(num1, num2):
#     return num1 % num2 == 0
# num1, num2 = int(input()), int(input())
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_numbers =  [2 * x for x in numbers]
# print(new_numbers)


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list[0][2][2].append(7000)
#
#
# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
#
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# # for i in list1:
# #     i.reverse()
# # print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     counter += len(i)
#     total += sum(i)
# print(total / counter)
# ----------------------------------------------------------------------
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = []
# for _ in range(n):
#     my_list.append([0] * m)
# print(my_list)
# __________________________________________________________________________

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
# for i in range(n):
#     my_list[i] = [0] * m
# print(my_list)
# _____________________________________________________________________________
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [[0] * m for _ in range(n)]
# print(my_list)
# __ обычный
# n, m = int(input()), int(input())
# s=[]
# for _ in range(n):
#     s.append([0]*m)
# print(s)
# -- ----------------------------------------лучший
# n, m = int(input()), int(input())
# s = [[0] * m for i in range(n)]
# print(s)

# самый плохой
# n, m = int(input()), int(input())
# s = [0] * n
# for i in range(n):
#     s[i] = [0] * m
# print(s)

# считываение
# n = 2                                          # количество строк (элементов)
# s = []
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     s.append(elem)
# print(s)

# n = 2
# s = []
# for i in range(n):
#     elem = [int(i) for i in input().split()]
#     s.append(elem)
# print(s)

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')   # используем необязательный параметр end
#     print()                             # перенос на новую строку


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:      # в один цикл
#     total += sum(row)
# print(total)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
# maximum = my_list[0][0]
# minimum = my_list[0][0]
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
# print(maximum + minimum)


# number = int(input())
# for _ in range(number):
#     list = []
#     for j in range(1, number + 1):
#         list.append(j)
#     print(list)


# n=int(input())
# s =[[int(j) for j in range(1,n+1)]for i in range(1,n+1)]
# print(*s, sep='\n')


# def chunked(symbols, n):
#     result = []
#     for i in range(0, len(symbols), n):
#         result.append(symbols[i:i + n])
#     return result
#
# symbols = input().split()
# n = int(input())
#
# print(chunked(symbols, n))


# n = input().split()
# o = [[]]
# k = 1
# while k != len(n) + 1:
#     for j in range(len(n)):
#         if len(n[j:j + k]) == k:
#             o.append(n[j:j + k])
#     k += 1
# print(o)



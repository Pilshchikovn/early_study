# num = int(input())
# flag = True
# while num > 9:
#     last = num % 10
#     num = num // 10
#     second = num % 10
#     if last != second and last > second:
#         flag = False
# if flag:
#     print('YES')
# else:
#     print('NO')

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10
#
# if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')
#

# n = int(input())
# for i in range(2, n + 1):
#     while n % i == 0:
#         print(i)
#     break
# for i in range(10000):
#     for j in range(500):
#         print('RITTA', end=' ')
#     print()

# from time import localtime, sleep
#
# for i in range(60):
#     x = localtime()
#     print('\n' + f'До конца рабочего дня осталось: {17 - x[3]} : {60 - x[4]}')
#     for j in range(60):
#         print(60 - j, end="*")
#         sleep(1)
#
# counter = 0
# for i_1 in range(9):
#     for i_2 in range(9):
#         for i_3 in range(9):
#             for i_4 in range(9):
#                 print(i_1, i_2, i_3, i_4)
#                 counter += 1
# print(counter)

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)



# for n in range(1,14):
#     for k in range(1,13):
#         for m in range(1,12):
#             if 28*n+30*k+31*m==365:
#                 print(n,k,m)


# for x in range(1, 10):
#     for y in range(1, 18):
#         for z in range(2, 99, 2):
#             if (x*10 + y*5 + z/2 == 100) and (x + y + z == 100):
#                 print(x, y, z)

# for x in range(1, 101):
#     for y in range(1, 101):
#         for z in range(1, 101):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 print('Быков:', x, 'Коров:', y, 'Телят:', z)


# for b in range(a + 1, 151):
#     for c in range(b + 1, 151):
#         for d in range(c + 1, 151):
#             e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
#             if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                 print(a + b + c + d + e)
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end="")
#     for j in range(i, 1, -1):
#         print(j - 1, end="")
#     print("")
#
# n = int(input())
# for i in range(1, n+1):
#     print(i, end = '')
#     for j in range(1, i+1):
#         if i%j == 0:
#             print('+', end = '')
#     print()
#
# n = int(input())
# factorial = 1
# for i in range(2, n + 1):
#     factorial *= i
# print(factorial)
#
# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

# n = int(input())
# s = 0
# while n > 10:
#     if n % 2 == 0:
#         s +=n
#     n //= 10
# else:
#     print(0)
# print(s)

# n = 7
# count = 0
# maximum = 0  #1000
# for i in range(1, n + 1):
#     x = int(input())
#     if x // 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n= int(input())
# for i in range(n):
#     if i == 1 or i == n:
#             print('*'*19, sep='', end='\n')
#     else:
#          print('*' + ' ' * 17 + '*')
#
#
#
# n = int(input())
# count3 = 0
# countLast = 0
# countChet = 0
# sumBig5 = 0
# multyBig7 = 1
# count05 = 0
# last = n % 10
# while n > 0:
#     x = n % 10
#     if x == 3:
#         count3 += 1
#     if x == last:
#         countLast += 1
#     if x % 2 == 0:
#         countChet += 1
#     if x > 5:
#         sumBig5 += x
#     if x > 7:
#         multyBig7 *= x
#     if x == 0 or x == 5:
#         count05 += 1
#     n //= 10
# print(count3)
# print(countLast)
# print(countChet)
# print(sumBig5)
# print(multyBig7)
# print(count05)


# import numpy as np
# from itertools import combinations
#
# numbers = np.arange(100)
# pairs = np.array(list(combinations(numbers, 2)))
# sums = np.apply_along_axis(lambda x: sum(x ** 3), 1, pairs)
#
# nums, counts = np.unique(sums, return_counts=True)
# print(*[num for num, count in zip(nums, counts) if count == 2][:5])
# import math
# n = int(input())
# count = 0
# for i in range(n):
#     count=(1+1/i)-math.log(n)
# print(count)

# flag = 'YES'
# for i in range(10):
#     a = int(input())
#     if a%2 != 0:
#         flag = 'NO'
# print(flag)

# fib=0
# n=int(input())
# for i in range(n+1):
#     a=int(input())
#     fib +=((a-1)+(a-2))
# print(fib)

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# a =input()
# for i in a:
#     while a !='КОНЕЦ' or a !='конец':
#         print(a, end='\n')
#         a =input()

# a =int(input())
# count=0
# while 1 <= a <=5:
#     if a==5:
#         count+=1
#     a =int(input())
# print(count)
#
# price = int(input())  # получаем цену услуги ведьмака
# count=0               # переменная для хранения кол-ва монет
#
# while price > 0:      # пока цена больше 0 выполняем цикл
#   if price >= 25:     # если цена больше или равен 25
#     price-=25         # вычитаем из нее 25
#   elif price >= 10:   # иначе проверяем остаток больше или равен 10
#     price-=10         # если да отнимаем 10
#   elif price >= 5:    # если остаток больше или равен 5
#     price-=5          # то вычитаем 5
#   else:               # иначе остается менее 5 и вычетаем по монетке
#     price-=1          # вычетаем по монетке
#   count+=1            # считаем кол-во монет, за один цикл вычитаем только 1 номинал монеты в зависимости от условий
#
# print(count)

# a = int(input())
# while a>0:
#     last = a%10
#     print(last,end=' ')
#     a = a//10
#
# x = str(input())
# print('Максимальная цифра равна', max(x))
# print('Минимальная цифра равна', min(x))
#
# n = int(input())
# maxx = 0  # в максимум берем минимальное число
# minn = 9  # в минимум берем максимальное число
#
# while n != 0:  # пока n не равна 0 выполняем цикл
#     if n % 10 > maxx:  # получаем последнюю цифру и сравниваем с максимальным
#         maxx = n % 10  # если последняя цифра больше то перезаписываем максимальное число
#     if n % 10 < minn:  # получаем последнюю цифру и сравниваем с минимальным
#         minn = n % 10  # если последняя цифра меньше то перезаписываем минимальное число
#     n = n // 10  # убираем последнюю цифру
#
# print('Максимальная цифра равна', maxx)
# print('Минимальная цифра равна', minn)  # put your python code here

num = int(input())
flag = True
while num > 9:
    last = num % 10
    num = num // 10
    sec = num % 10
    if last != sec:
        flag = False
if flag:                
    print('YES')
else:
    print('NO')
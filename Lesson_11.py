# # s = input().split()
# # d = {}
# # for x in s:
# #     x = x.split('=')
# #     d[x[0]] = int(x[1])
# #
# # print(*sorted(d.items()))
# #
# #
# # lst_in = input().split()
# # d = dict(i.split('=') for i in lst_in)
# # if 'house' in d  and 'True' in d and '5' in d:
# #     print('ДА')
# # else:
# #     print('НЕТ')
#
# # i = '*'
# # fot i in range(8):
# #     print(i+=1)
#
#
# # При помощи операции нахождения остатка и целочисленного деления можно достаточно несложно вычислить любую цифру числа.
# #
# # Рассмотрим программу получения цифр двузначного числа:
# #
# # num = 17
# # a = num % 10
# # b = num // 10
# # print(a)
# # print(b)
# # Результатом выполнения программы будут два числа:
# #
# # 7
# # 1
# # То есть сначала мы вывели последнюю цифру числа, а затем первую цифру.
# #
# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(f'Сумма цифр = {a+b+c}, Произведение цифр = {a*b*c}', sep='\n')
#
# num = int(input())
# c = num % 10
# b = (num % 100) // 10
# a = num // 100
#
# print(a,b,c,sep='')
# print(a,c,b,sep='')
# print(b,a,c,sep='')
# print(b,c,a,sep='')
# print(c,a,b,sep='')
# print(c,b,a,sep='')
#
# m = int(input())
# m1 = m // 1000
# m2 = (m // 100) % 10
# m3 = (m // 10) % 10
# m4 = m % 10
# print("Цифра в позиции тысяч равна", m1)
# print("Цифра в позиции сотен равна", m2)
# print("Цифра в позиции десятков равна", m3)
# print("Цифра в позиции единиц равна", m4)

# a, b, s= int(input()), int(input()),input()
# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
# else:
#     print(a / b)
# else:
#     print('Неверная операция')

# a = int(input())
# if a == 0:
#     print('зеленый')
# elif a in range(1,11) and a%2==1:
#     print('красный')
# elif a in range(1,11) and a%2==0:
#     print('черный')
# elif a in range(1,19) and a%2==0:
#     print('красный')
# elif a in range(1,19) and a%2==1:
#     print('черный')
# elif a in range(19,29) and a%2==1:
#     print('красный')
# elif a in range(19,29) and a%2==0:
#     print('черный')
# elif a in range(29,37) and a%2==0:
#     print('красный')
# elif a in range(29,37) and a%2==1:
#     print('черный')
# else:
#     print('ошибка ввода')
#
# a = int(input())
# if a==1:
#     print('I')
# elif a==2:
#     print('II')
# elif a==3:
#     print('III')
# elif a==4:
#     print('IV')
# elif a==5:
#     print('V')
# elif a==6:
#     print('VI')
# elif a==7:
#     print('VII')
# elif a==8:
#     print('VII')
# elif a==9:
#     print('IX')
# elif a==10:
#     print('X')
# else:
#     print('ошибка')

# a = float(input())
# if a == 0:
#     print('Обратного числа не существует')
# else:
#     print(a ** -1)


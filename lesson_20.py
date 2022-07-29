# q = int(input())
# i = 0
# ii = 0
# iii = 0
# iiii = 0
# for k in range(q):
#     x, y = map(int, input().split())
#     if x != 0 and y != 0:
#         if x>0 and y>0:
#            i+=1
#         elif x>0 and y<0:
#             iiii+=1
#         elif x<0 and y<0:
#             iii+=1
#         elif x<0 and y>0:
#             ii+=1
# print(f'Первая четверть: {i}')
# print(f'Вторая четверть: {ii}')
# print(f'Третья четверть: {iii}')
# print(f'Четвертая четверть: {iiii}')

# n = list(input().split())
# n.insert(0,n.pop(-1))
# print(*n)

# a=input()
# b=input()
# if a == "камень" and b == "ножницы":
#     print("Тимур")
# elif  a == "ножницы" and b == "бумага":   #
#     print("Тимур")
# elif  a == "бумага" and b == "камень": #
#     print("Тимур")
# elif  a == "камень" and b == "ящерица":  #
#     print("Тимур")
# elif  a == "ящерица" and b == "Спок":  #
#     print("Тимур")
# elif  a == "ножницы" and b == "ящерица":
#     print("Тимур")
# elif  a == "ящерица" and b == "бумага":
#     print("Тимур")
# elif  a == "Спок" and b == "ножницы":
#     print("Тимур")
# elif  a == "Спок" and b == "камень":
#     print("Тимур")
# # в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы
# elif  a == b:
#     print("ничья")
# else:
#     print("Руслан")


# word = input() + ' запретил букву'
# for i in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
#     if i in word:
#         print(word, i)
#         word = word.replace(i, '').strip().replace('  ', ' ')









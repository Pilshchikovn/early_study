# lst = list(map(int, input().split()))
#
# for i, value in enumerate(lst):
#     lst[i] = value ** 2
#
# print(*lst)


# lst = list(map(int, input().split()))
# for i, d in enumerate(lst):
#     print(lst[i], d, end=' ')

# n = list(map(float, input().split()))
# s = float()
#

# lst = list(map(float, input().split()))
# res = lst[0]
# for i in lst:
#     if i < res:
#         res = i
# print(res)
#
# digs = list(map(float, input().split()))
# for i, d in enumerate(digs):
#     if d < 0:
#         digs[i] = -1.0
# print(*digs)

# если нужно получить список из строк, например
# ['Москва', 'Лондон', 'Берлин']
# то  всегда достаточно
# n = input().split()
# первый вариант будет избыточным, так как вернёт тоже самое.
#  Такой вариант:
# n = list(map(int, input().split()))
# используется, когда нужно преобразовать строку в какой-то другой тип данных.
# например:
# ['123', '234', '345']  -->  [123, 234, 345]

# lst = list(map(str, input().split()))
# b = iter(lst)
# print(next(b))
# print(next(b))

# lst =input().split()
# b = iter(lst)
# print(next(b))

# for i in iter(input()):
#     print(i, end=' ')
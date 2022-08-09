# class Lion:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'The object Lion {self.name}'
#
#
# simba = Lion('simba')
# print(simba.name)

# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         if gender == 'male' or gender == 'female':
#             self.gender = gender
#         else:
#             print(f'?? ????, ??? ?? ????? ?????? ????? ??? ????? ???????!')
#             self.gender='male'
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f'????????? {self.surname} {self.name}'
#         if self.gender == 'female':
#             return f'????????? {self.surname} {self.name}'
#
#
# p1 = Person('Chuck', 'Norris')
# print(p1) # ???????? "????????? Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # ???????? "????????? Kunis Mila"
# p3 = Person('???-???', '??????', True)# ???????? "?? ????, ??? ?? ????? ?????? ????? ??? ????? ???????!"
# print(p3) # ???????? "????????? ?????? ???-???"

# class Vector:
#     def __init__(self,*args):
#         self.args=args
#         self.values = sorted(list(filter(lambda x: isinstance(x, int), args)))
#     def __repr__(self):
#         if len(self.values) >0:
#             return f'Вектор{tuple(self.values)}'
#         else:
#             return f'Пустой вектор'

# class Vector:
#     def __init__(self, *args):
#         self.values = [i for i in args if type(i) == int]
#
#     def __repr__(self):
#         return self.values
#
#     def __str__(self):
#         return f'Вектор{tuple(sorted(self.values))}' if self.values != [] else 'Пустой вектор'
#
#
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор"

# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#
#     def __add__(self, other):
#         print('__add__ was called')
#         if isinstance(other,Bankaccount):
#             return self.balance +other.balance
#         if isinstance(other,(int,float)):
#             return  self.balance +other
#         raise NotImplemented
# c= Bankaccount('nikita',100)
# x= Bankaccount('dg',99)
# print(c + x)


# from functools import total_ordering
# @total_ordering
# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.balance = name
#         self.surname=surname
#         self.rating=rating
#
#     def __eq__(self, other):
#         if isinstance(other, ChessPlayer) :
#             return self.rating == other.rating
#         elif isinstance(other, int):
#             return self.rating == other
#         else:
#             print(f'Невозможно выполнить сравнение')
#
#     def __lt__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         elif isinstance(other, int):
#             return self.rating < other
#         else:
#             print(f'Невозможно выполнить сравнение')
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"

# class City:
#     def __init__(self,name):
#         self.name=str(name).title()
#     def __str__(self):
#         return f'{self.name}'
#     def __bool__(self):
#         s= ['a', 'e', 'i', 'o', 'u']
#         for i in s:
#             if self.name.endswith(i):
#                 return False
#         return True
# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"

class Quadrilateral:
    def __init__(self, *args):
        self.width = args[0]
        self.height = args[-1]

    def __str__(self):
        if self.width ==self.height:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"

# @staticmethod
# def clear():
#     print('Очищаем корзину')
#     for i in Trash.content:
#         File.remove(i)
#     Trash.content = []
#     print('Корзина пуста')
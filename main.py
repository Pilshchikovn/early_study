#
# class MyClass():
#
#     TOTAL_OBJECTS =0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS +1
#
#     @classmethod
#     def total_objects(cls):
#         print("Total objects: " ,cls.TOTAL_OBJECTS)
# # Создаем объекты
# my_obj1 = MyClass()
# my_obj2 = MyClass()
# my_obj3 = MyClass()
# # Вызываем classmethod
# MyClass.total_objects()

# class User:
#     def __init__(self,name, role):
#         self.name = name
#         self.role = role
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(x):
#         return True if x.role in Access.__access_list else False
#
#     @staticmethod
#     def get_access(y):
#         if isinstance(y, User):
#             if Access.__check_access(y):
#                 print(f'User {y.name}: success')
#             else:
#                 print(f'AccessDenied')
#         else:
#             print(f'AccessTypeError')


#
# user1 = User('batya99', 'admin')
# Access.get_access(user1)  # печатает "User batya99: success"
# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya)  # печатает AccessDenied
# Access.get_access(5)  # печатает AccessTypeErro
#
# from functools import total_ordering
#
#
# @total_ordering
# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.balance = name
#         self.surname = surname
#         self.rating = rating
#
#     def __eq__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         elif isinstance(other, int):
#             return self.rating == other
#         else:
#             return f'Невозможно выполнить сравнение'
#     def __gt__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         elif isinstance(other, int):
#             return self.rating > other
#         else:
#             return f'Невозможно выполнить сравнение'
#
#     def __lt__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         elif isinstance(other, int):
#             return self.rating < other
#         else:
#             return f'Невозможно выполнить сравнение'
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000)  # False
# print(ian == 2789)  # True
# print(magnus == ian)  # False
# print(magnus > ian)  # True
# print(magnus < ian)  # False
# print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"


# def pes(func):
#     print("Подключение к хранилищу")
#     func()
#     print("Отключение от хранилища")
#
# @pes
# def upload_file():
#     print("111.")

import time
from time import perf_counter


# class Timer:
#
#     def __init__(self, func) -> None:
#         self.func = func
#
#     def __call__(self, *args, **kwargs) -> None:
#         start = perf_counter()
#         self.func(*args, **kwargs)
#         finish = perf_counter()
#         print(f'Время работы программы {self.func.__name__}: {finish - start}')

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True


emp1 = Person("vasya")
print(emp1.get_name(), emp1.is_employee())  # vasya False

emp2 = Employee("gena bukin")
print(emp2.get_name(), emp2.is_employee())  # gena bukin True
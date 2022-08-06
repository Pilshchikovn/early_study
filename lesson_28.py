# class Car:
#     '''Класс для определения
#     характеристик машин'''
#     model = 'BMW'
#     engine = 1.6
# a = Car()
# b= Car()
# b.engine=2.0
# b.color='white'
# print(b.engine,b.color)
# print(type(b))

# class Person:
#     name='Ivan'
#     age=30
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
# print(getattr(Book,'writer'))
# print(getattr(Book,'pages'))
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
# setattr(Book,'name','Скотный двор')
# setattr(Book,'pages',115)

# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
# setattr(Book,'rating',8.7)
# Book.genre = 'dystopian'

# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#     rating = 8.7
#     genre = 'dystopian'
#
#
# delattr(Book, 'pages')
# del Book.writer
# del Book.rating
# print(Book.__dict__)

# class Cat:
#     name = 'Матроскин'
#     color = 'black'
#
# a = Cat()
# my_cat = a


# class Car:
#     model = 'BMW'
#     engine = 1.6
#
# a1= Car()
# a2=Car()
# a1.seat=4
# a1.model='njk'
# del a1.model
# print(a1.model)


# class SuperHero:
#     '''SuperHero class'''
#     pass
#
#
# batman = SuperHero()
# batman.can_fly = False
# batman.damage = 175
#
# superman = SuperHero()
# superman.can_fly = True
# superman.damage = 285
# superman.alter_ego = 'Кларк Кент'

# class Car:
#     model = 'BMW'
#     engine = 1.6
#
#     @staticmethod
#     def drive():
#         print("Let's go")
# Car.drive()
# a=Car()
# a.drive()
# class Car:
#     "Класс для определения характеристик машин"
#     model = "BMW"
#     engine = 1.6
#
#     def drive(self):
#         print(f"Let's go: {self}")
#
#
# a = Car()  # Создаём экземпляр класса
# b = Car()  # Создаём экземпляр класса
# a.drive()  # Вызываем метод класса
# b.drive()  # Вызываем метод класса

# class Lion:
#     def roar(self):
#         print('Rrrrrrr!!!')
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!


# class Robot:
#     def set_name(self, name):
#         self.name = name
#
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print('У робота нет имени')
#
#     def say_bye(self):
#         print('See u later alligator')


# class Counter():
#     def start_from(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(f"Текущее значение счетчика = {self.value}")
#
#     def reset(self):
#         self.value = 0
#
#
# c2 = Counter()
# c2.start_from(3)
# c2.display()  # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display()  # печатает "Текущее значение счетчика = 4"

'''Создайте класс Constructor, в котором реализованы

метод add_atribute , принимающий на вход название атрибута в виде строки и его значение.
При помощи функции setattr необходимо создать или изменить атрибут для ЭК, у которого этот метод был вызван
метод display ,  печатающий на экран словарь __dict__ у ЭК
Пример работы с классом Constructor'''

# class Constructor:
#
#     def add_atribute(self, name, value):
#         setattr(self, name, value)
#     def display(self):
#         print(self.__dict__)
#
# x= Constructor()
# x.add_atribute('oleg',100)
# x.display()


# '''Создайте класс Point. У этого класса должны быть
#
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр
# класса соответственно в атрибуты x и y
# метод get_distance, который обязательно принимает экземпляр класса
# Point и возвращает расстояние между двумя точками по теореме Пифагора.
#  В случае, если в данный метод передается не экземпляр класса Point необходимо
#  вывести сообщение "Передана не точка"'''

# class Point:
#     def set_coordinates(self,x,y):
#         self.x=x
#         self.y=y
#     def get_distance(self,object):
#         if isinstance(object, Point):
#             return ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5
#         else:
#             print('Передана не точка')
#
# class Constructor:
#
#     def add_atribute(self, name, value):
#         setattr(self, name, value)
#     def display(self):
#         print(self.__dict__)


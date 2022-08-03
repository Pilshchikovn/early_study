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


''' Создайте класс Robot, в котором реализованы
метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
метод say_bye ,  печатающий на экран фразу «See u later alligator»
После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
Затем вызовите у переменной  c3po сперва метод say_hello , а затем метод say_bye
И тоже самое сделайте с переменной r2d2: сперва вызывайте метод say_hello , потом - метод say_bye'''


class Robor:
    def say_hello(self):
        print('Hello, human! My name is C-3PO')

    def say_bye(self):
        print('See u later alligator')

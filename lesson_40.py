# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.age = 50
#
#     def __str__(self):
#         return f'Person {self.name} {self.surname}'
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname)
#         self.age = age
#
#
#     # Вызываем родительский метод __str__, передавая ему объект текущего класса.
#     def __str__(self):
#         return super().__str__()
#
# p = Person('Ivan', 'Ivanov')
# d = Doctor('Petr', 'Petrov', 25)
# print(d) # Person Petr Petrov, что соответсвует имени ЭК Doctor.

# class Person:
#     def __init__(self, name, passport):
#         self.name = name
#         self.passport = passport
#
#     def display(self):
#         print(f'{self.name}: {self.passport}')
#
#
# class Employee(Person):
#     def __init__(self, name, passport, salary, department):
#         super().__init__(name, passport)
#         self.salary = salary
#         self.department = department
# a = Employee('Raul', 886012, 200000, "QA")
# a.display()  # печатает "Raul: 886012"


# class Vehicle:
#
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
#     def display(self):
#         print(f'Total {self.name} fare is: {self.fare()}')
#
#
# class Bus(Vehicle):
#     def __init__(self, name, mileage, capacity=50):
#         super().__init__(name, mileage, capacity)
#
#     def fare(self):
#         return super().fare() * 1.1
#
#
# class Taxi(Vehicle):
#
#     def __init__(self, name, mileage, capacity=4):
#         super().__init__(name, mileage, capacity)
#
#     def fare(self):
#         return super().fare() * 1.35
#
# sc = Vehicle('Scooter', 100, 2)
# sc.display()  # печатает: Total Scooter fare is: 200
#
# merc = Bus("Mercedes", 120000)
# merc.display()  # печатает: Total Mercedes fare is: 5500.0
#
# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()  # печатает: Total Volkswagen Polo fare is: 540.0

# class Transport:
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
#
#
# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue):
#         super().__init__(brand, max_speed, kind='Car')
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue
#
#     @property
#     def gasoline(self):
#         return f'Осталось бензина на {self.__gasoline_residue} км'
#
#     @gasoline.setter
#     def gasoline(self, value):
#         if isinstance(value, int):
#             self.__gasoline_residue += value
#             print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
#         else:
#             print(f'Ошибка заправки автомобиля')
#
#
# class Boat(Transport):
#     def __init__(self, brand, max_speed,owners_name):
#         super().__init__(brand, max_speed, kind='Boat')
#         self.owners_name=owners_name
#
#     def __str__(self):
#         return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
#
#
# class Plane(Transport):
#     def __init__(self, brand, max_speed, capacity):
#         super().__init__(brand, max_speed, kind='Plane')
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#
#
# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

# class Initialization:
#     def __init__(self, capacity: int, food: list):
#
#         if isinstance(capacity, int):
#             self.capacity = capacity
#             self.food = food
#         else:
#             print('Количество людей должно быть целым числом')
#
#
# class Vegetarian(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
#
# class MeatEater(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'
#
#
# class SweetTooth(Initialization):
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return other == self.capacity
#         elif isinstance(other, (Vegetarian, MeatEater, SweetTooth)):
#             return self.capacity == other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return other > self.capacity
#         elif isinstance(other, (Vegetarian, MeatEater, SweetTooth)):
#             return self.capacity < other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return other < self.capacity
#         elif isinstance(other, (Vegetarian, MeatEater, SweetTooth)):
#             return self.capacity > other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#
# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > v_first)  # True
# print(30000 == s_first)  # True
# print(s_first == 25000)  # False
# print(100000 < s_first)  # False
# print(100 < s_first)  # True

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee(Person, Company):
#     def __init__(self, name, age, company_name, location):
#         super().__init__(name, age)
#         Company.__init__(self, company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# emp.display_person_info()
# emp.display_company_info()

# class First(object):
#     def __init__(self):
#         print("First(): entering")
#         super(First, self).__init__()
#         print("First(): exiting")
#
#
# class Second(object):
#     def __init__(self):
#         print("Second(): entering")
#         super(Second, self).__init__()
#         print("Second(): exiting")
#
#
# class Third(First, Second):
#     def __init__(self):
#         print("Third(): entering")
#         super(Third, self).__init__()
#         print("Third(): exiting")
#
#
# Third()
#
# print(Third.__mro__)

class PointSlots:
    __slots__ = ('x', 'y')  # Перечисляем все возможные атрибуты экземпляров класса

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
p2.x = 10  # AttributeError: 'PointSlots' object has no attribute 'new_attr'
# p2.zzz=10500
print(p2.__dict__)


from timeit import timeit

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_time_point():
    p1 = Point(3, 4)
    p1.x = 100
    p1.x
    del p1.x


def test_time_pointslots():
    p1 = Point(3, 4)
    p1.x = 100
    p1.x
    del p1.x


print('No __slots__ stopped:', timeit(test_time_point))
print('__slots__ stopped:', timeit(test_time_pointslots))

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print('No slots:', s.__sizeof__(), s.__dict__.__sizeof__()) # No slots: 32 88
d = PointSlots(3, 4)
print('Slots', d.__sizeof__()) # Slots 32

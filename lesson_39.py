# class Vehicle:
#     def __init__(self,name, max_speed,mileage):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage
#
#     def display_info(self):
#         print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')
#
#
# class Bus(Vehicle):
#     pass
#
# bus_99 = Bus("Ikarus", 66, 124567)
# bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"
#
#
# class Plane(Vehicle):
#     pass
#
#
# class Boat(Vehicle):
#     pass
#
#
# class RaceCar(Car):
#     pass

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def is_employee(self):
#         return False
#
#
# class Employee(Person):
#     def is_employee(self):
#         return True
#
#
# emp1 = Person("vasya")
# print(emp1.get_name(), emp1.is_employee())  # vasya False
#
# emp2 = Employee("gena bukin")
# print(emp2.get_name(), emp2.is_employee())  # gena bukin True
#
# class NewInt(int):
#     def repeat(self, n=2):
#         s= str(self) * n
#         return int(s)
#
#     def to_bin(self):
#         return int(bin(self)[2:])
#
#
# a = NewInt(9)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3))  # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin())  # печатает 100011 - двоичное представление числа 35
# print(NewInt())



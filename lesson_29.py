# class Vehicle:
#     def __init__(self,max_speed, mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)# 240 18

# class Laptop:
#     def __init__(self, brand, model, price, laptop_name):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = laptop_name
#         self.laptop_name = self.brand + " " + self.model
#
#
# laptop1 = Laptop('hp', '15-bw0xx', 57000)
# laptop2 = Laptop('hp', '15-bw0xx', 57000)


# class SoccerPlayer:
#     def __init__(self, name, surname, goals=0, assists=0):
#         self.name = name
#         self.surname = surname
#         self.goals = goals
#         self.assists = assists
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics()
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics()
# print(leo.__dict__)
#
# class Zebra():
#     def __init__(self, count=0):
#         self.count = count
#
#     def which_stripe(self):
#         if self.count % 2 == 0:
#             print('Полоска белая')
#         elif self.count % 2 != 0:
#             print('Полоска черная')
#         self.count += 1
# class Zebra:
#     def __init__(self):
#         self.a = 'Полоска белая'
#         self.b = 'Полоска черная'
#
#     def which_stripe(self):
#         print(self.a)
#         self.a, self.b = self.b, self.a

# z1 = Zebra()
# z1.which_stripe()  # печатает "Полоска белая"
# z1.which_stripe()  # печатает "Полоска черная"
# z1.which_stripe()  # печатает "Полоска белая"

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         full_name = self.last_name + ' ' + self.first_name
#         return str(full_name)
#
#     def is_adult(self):
#         return self.age >= 18
#
#
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult())  # выводит "True"


# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#     def speak(self, x):
#         return f'{self.name} says {x}'
# jack = Dog("Jack", 4)
# print(jack.description())  # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof"))  # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow"))  # распечатает 'Jack says Bow Wow''''


# class Stack:
#
#     def __init__(self,values=[]):
#         self.values=values
#
#     def push(self,item):
#         self.values.append(item)
#     def pop(self):
#         if len(self.values)>0:
#             return self.values.pop(-1)
#         else:
#             print('Empty Stack')
#     def peek(self):
#         if len(self.values)>0:
#             return self.values[-1]
#         else:
#             print('Empty Stack')
#             return None
#     def is_empty(self):
#         return True if len(self.values)==0 else False
#     def size(self):
#         return len(self.values)
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2'''


# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# class Worker:
#     def __init__(self,name, salary, gender, passport):
#         self.name=name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')

# worker_objects=[]
# for i in persons:
#     worker_objects.append(Worker(i[0], i[1], i[2],i[3]))
#
# for i in worker_objects:
#     i.get_info()

# worker_objects = [Worker(*i) for i in persons]
# [worker.get_info() for worker in worker_objects]
# print(type(worker_objects))
# bob = Worker('Bob Moore', 330000, 'M', '1635777202')
# bob.get_info()


# class CustomLabel:
#     def __init__(self,text,**kwargs):
#         self.text=text
#         for key, value in kwargs.items():
#             self.__dict__[key] = value
#
#     def config(self,**kwargs):
#         self.__dict__.update(kwargs)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()

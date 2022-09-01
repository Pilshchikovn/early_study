# c=[1,2,3].__iter__()
# print(c.__next__())
# print(c.__next__())

# class Student:
#     def __init__(self,name,surname,marks):
#         self.name=name
#         self.surname=surname
#         self.marks=marks
#     def __getitem__(self, item):
#         return self.name[item]
#
#     def __iter__(self):
#         print('call iter')
#         self.index=0
#         return self
#
#     def __next__(self):
#         letter =self.name[self.index]
#         self.index+=1
#         return letter
#
# s =Student('maxim','df',[2,3,4,5])
# for i in s:
#     print(i)
# class Marks:
#     def __init__(self, values):
#         self.values = values
#         self.index = 0
#
#     def __iter__(self):
#         print('call iter Mark')
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.values):
#             self.index = 0
#             raise StopIteration
#         mark = self.values[self.index]
#         self.index += 1
#         return f'call next, mark = {mark}'
#
#
# class Student:
#     def __init__(self, name, surname, marks):
#         self.name = name
#         self.surname = surname
#         self.marks = marks
#
#     def __iter__(self):
#         print('call iter Student')
#         self.index = 0
#         return self.marks

# def __next__(self):
#     if self.index >= len(self.marks):
#         raise StopIteration
#     res = self.marks[self.index]
#     self.index += 1
#     return f'call next Student = {res}'

#
# misha_marks = Marks([3, 4, 5])
# misha = Student('Misha', 'Ivanov', misha_marks)
# for m in misha:
#     print(m)

# class PowerTwo:
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         2**self.number
#
#
# numbers = PowerTwo(2)
#
# iterator = iter(numbers)
#
# print(next(iterator)) # печатает 1
# print(next(iterator)) # печатает 2
# print(next(iterator)) # печатает 4
# print(next(iterator)) # исключение StopIteration

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)
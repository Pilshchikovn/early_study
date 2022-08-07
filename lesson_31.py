# class Square:
#     def __init__(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print('calculate area')
#             self.__area = self.__side ** 2
#         return self.__area

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     @property
#     def area(self):
#         return self.width*self.length
# a=Rectangle(8,10)
# print(a.area)

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @property
#     def date(self):
#         return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"
#
#     @property
#     def usa_date(self):
#         return f"{self.month:02d}-{self.day:02d}-{self.year:04d}"
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
#
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999

# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Робот {self.name} был создан')
#         Robot.population += 1
#
#     def destroy(self):
#         Robot.population -= 1
#         print(f'Робот {self.name} был уничтожен')
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(cls):
#         print(f'{cls.population}, вот сколько нас еще осталось')
#
#
# r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
# r2.say_hello()  # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many()  # печатает "1, вот сколько нас еще осталось"
# r2.destroy()  # печатает "Робот R2-D2 был уничтожен"

# class User:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
# class Access:
#     def __init__(self):
#         __access_list = ['admin', 'developer']
#     @staticmethod
#     def __check_access(role):
#         return role in Access.__access_list
#     @staticmethod
#     def get_access():
#         if isinstance(User.role, User):
#             if Access.__check_access:
#                 print(f'User : success')
#             else:
#                 print(f'AccessDenied')
#         else:
#             print(f'AccessDenied')
#
# user1 = User('batya99', 'admin')
# Access.get_access(user1) # печатает "User batya99: success"
#
# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied
#
# Access.get_access(5) # печатает AccessTypeErro


from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property
    def password(self):
        print('getter called')
        return self.__password

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Len<4')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать цифру')
        self.__password = value


s = User('df', 34)
print(s.password)
s.password = 'nbhjhb8j'
print(s.password)

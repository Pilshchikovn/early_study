# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(x):
#         return x in Access.__access_list
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

from string import digits
from string import ascii_lowercase,ascii_uppercase
s=input()
for i in ascii_lowercase:
    for j in ascii_uppercase:
        if i,j in s:
            print('Ok')


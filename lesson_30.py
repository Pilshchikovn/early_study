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
#     __shared_attr = {'breed': 'pers','color': 'black'}
#     def __init__(self,name, salary, gender, passport):
#         self.name=name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#         self.__dict__=Worker.__shared_attr
#
#     # def get_info(self):
#     #     print(f'Worker {self.name}; passport-{self.passport}')
#
# # worker_objects = [Worker(*i) for i in persons]
# # [worker.get_info() for worker in worker_objects]
# sam =Worker('Sam', 403445, 'M', '0602870126')
# gam =Worker('Gam', 403445, 'M', '0602870126')
# print(sam.__dict__)
# print(gam.__dict__)
# sam.breed = 'siam'
# print(sam.__dict__)
# print(gam.__dict__)
# gam.color = 'sinii'

# class Bankaccount:
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     def print_public_data(self):
#         print(self.name, self.balance, self.passport)
#
#     def print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
#
# account1 = Bankaccount('Bob', 1000, 3610)
# # print(account1.print_public_data())
# print(account1.print_private_data())
# print(account1.__name)

# class Student:
#     def __init__(self,name, age, branch):
#         self.__name = name
#         self.__age =age
#         self.__branch =branch
#     def __display_details(self):
#         print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')
#     def access_private_method(self):
#         self.__display_details()
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()

# class PizzaMaker:
#     def __make_pepperoni(self):
#         print('ok')
#
#     def _make_barbecue(self):
#         print('olo')
# maker = PizzaMaker()
# print(maker._make_barbecue())
# print(maker._PizzaMaker__make_pepperoni())


#

# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#     def get_email(self):
#         return self.__email
#     def set_email(self,value):
#         if value.count('@')==1 and '.' in value[value.find('@'):] and isinstance(value,str):
#             self.__email=value
#         else:
#             print(f'ErrorMail:{value}')
#
#     email = property(fget=get_email,fset=set_email)
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
# k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait


# class Bankaccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         return self.__balance
#     @my_balance.setter
#     def my_balance(self, value):
#         if not isinstance(value, (int, float)):
#             return ValueError('Balance must be number')
#         self.__balance = value
#     @my_balance.deleter
#     def del_balance(self):
#         del self.__balance
#
#     # balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)
#     # my_balance = property(get_balance)
#     # my_balance = my_balance.getter(get_balance)
#     # my_balance = my_balance.setter(set_balance)
#     # my_balance = my_balance.deleter(del_balance)
#
#
# vasya = Bankaccount('vasya', 100)
# print(vasya.get_balance())
# print(vasya.set_balance(500))
# print(vasya.get_balance())
# print(vasya.__dict__)
# vasya.balance = 10000
# print(vasya.get_balance())
# print(vasya.balance)

class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for i, k in enumerate(self._notes,1):
            print(f'{i}.{k}')
        # s = [i for i in enumerate(self._notes, 1)]
        # print(*s,sep ='\n')

    @notes_list.setter
    def notes_list(self, value):
        self._notes = value


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list

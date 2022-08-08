class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, payment):
        if self.__balance >= payment:
            self.__balance -= payment
            return True
        else:
            print(f'Не хватает средств на балансе. Пополните счет')
            return False


class Cart:
    def __init__(self, login, balance):
        self.user = User(login, balance)
        self.goods = {}
        self.__total = 0
    def add (self, goods=1):




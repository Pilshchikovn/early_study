# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f"I am a cat. My name is {self.name}.")
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f"I am a dog. My name is {self.name}.")
#
#     def make_sound(self):
#         print("Bark")
#
#
# cat_obj = Cat("Ren")
# dog_obj = Dog("Stimpy")
#
# for animal in (cat_obj, dog_obj):
#     animal.make_sound()
#     animal.info()

# class UnitedKingdom:
#     @staticmethod
#     def capital():
#         print('London is the capital of Great Britain.')
#
#     @staticmethod
#     def language():
#         print(f'English is the primary language of Great Britain.')
#
#
# class Spain:
#     @staticmethod
#     def capital():
#         print('Madrid is the capital of Spain.')
#
#     @staticmethod
#     def language():
#         print(f'Spanish is the primary language of Spain.')
#
# obj_uk = UnitedKingdom()
# obj_spa = Spain()
# for country in (obj_spa, obj_uk):
#     country.capital()
#     country.language()


class Building:
    def __init__(self, number):
        self.number = list(range(number + 1))

    def __repr__(self):
        return str(self.number)

    def __getitem__(self, item):
        if 0 <= item <= len(self.number):
            return self.number[item]
        else:
            return None

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.number):
            self.number[key] = value
        else:
            raise IndexError('Index out if range')

    def __delitem__(self, key):
        if 0 <= key <= len(self.number):
            self.number[key] = None
        else:
            raise IndexError('Index out if range')


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
print(iron_building)

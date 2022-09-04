# #1
# info = dict(name = 'Timur', age = 28, job = 'Teacher')
# print(info)
# #2
# info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
# info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
# # 3

# dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
# print(dict1)
#4
# languages = {'Python': 'Гвидо ван Россум',
#              'C#': 'Андерс Хейлсберг',
#              'Java': 'Джеймс Гослинг'}
#
# info = dict(name = 'Timur', age = 28, job = 'Teacher')
#
# print(languages)
# print(info)

# info = {'name': 'Timur',
#         'age': 28,
#         'job': 'Teacher',
#         'city': 'Moscow',
#         'email': 'timyr-guev@yandex.ru'}
#
# print(info['name'])
# print(info['email'])

# keys = ['name', 'age', 'job', 'length']
# values = ['Timur', 28, 'Teacher']
# info = dict(zip(keys, values))
# print(info)

# my_dict = dict.fromkeys(['a', 'b', 'c'], -1)
# print(my_dict['b'])

# my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
# print(my_dict[2][1])

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i in capitals:
#     print(i)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i in capitals:
#     print(capitals[i])

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(i)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i in capitals.values():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(i)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i in capitals.items():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(i)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for i, j in capitals.items():
#     print(i, '-', j)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# print(*capitals, sep='\n')

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
#
# a=[]
# for i in users:
#     if i['phone'][-1]=='8':
#         a.append(i['name'])
# print(*sorted(a))
#
#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# result = [i['name'] for i in users if i['phone'].endswith('8')]
#
# print(*sorted(result))
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

#1

# s = []
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         s.append(i['name'])
# print(*sorted(s))
#2

# result = [i['name'] for i in users if 'email' not in i or i['email'] == '']
# print(*sorted(result))

#
# d = {
#           '0': 'zero',
#           '1': 'one',
#           '2': 'two',
#           '3': 'three',
#           '4': 'four',
#           '5': 'five',
#           '6': 'six',
#           '7': 'seven',
#           '8': 'eight',
#           '9': 'nine'
#          }
# for i in input():
#     print(d[i], end=' ')

#2

# print(*[d[i] for i in input()])


# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# s = input()
# print(d[s])


# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# s = input()
# print(f'{s}: {d[s]}')

# d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
#
# print(*[d[i] for i in input().upper().replace('"', '')], sep='')

# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for i in input().upper():
#     for key, value in keyboard.items():
#         if i in value:
#             print(key * (value.index(i) + 1), end="")

# keys_mapping = {
#     'A': '.-',
#     'B': '-...',
#     'C': '-.-.',
#     'D': '-..',
#     'E': '.',
#     'F': '..-.',
#     'G': '--.',
#     'H': '....',
#     'I': '..',
#     'J': '.---',
#     'K': '-.-',
#     'L': '.-..',
#     'M': '--',
#     'N': '-.',
#     'O': '---',
#     'P': '.--.',
#     'Q': '--.-',
#     'R': '.-.',
#     'S': '...',
#     'T': '-',
#     'U': '..-',
#     'V': '...-',
#     'W': '.--',
#     'X': '-..-',
#     'Y': '-.--',
#     'Z': '--..',
#     '0': '-----',
#     '1': '.----',
#     '2': '..---',
#     '3': '...--',
#     '4': '....-',
#     '5': '.....',
#     '6': '-....',
#     '7': '--...',
#     '8': '---..',
#     '9': '----.',
# }
# # print(*[keys_mapping[i] for i in input().upper()], end='')
#
#
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
#          '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-',
#          '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
#          '....-', '.....', '-....', '--...', '---..', '----.']
# s = dict(zip(letters, morse))
# print(*[s[i] for i in input().upper() if i in s], end='')

# result = {}
# s=[i for i in range(1,16)]
# s1=[i**2 for i in range(1,16)]
# d=dict(zip(s,s1))
# print(d)

# result = {}
# for i in range(1, 16):
#     result[i] = i * i
# print(result)

# result = dict(zip(range(1, 16), [i * i for i in range(1, 16)]))

# result = {}
# for i in range(1, 16):
#     result.setdefault(i, i**2)

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# print(text.count('f'))
# result = {}
# for i in text:
#     result[i] = result.get(i, 0) + 1
# print(result)

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {}
# for i in s.split():
#     result[i] = result.get(i, 0) + 1
# res = [i for i in result if result[i] == max(result.values())]
# print(sorted(res)[0])

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

# dog=[]
# dog_owner=[]
# for i in pets:
#     dog.append(i[0])
#     dog_owner.append(tuple(i[1:]))
# result= dict(zip(dog_owner,list(dog)))
# print(result)


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for pet, *dog_owner in pets:
#     result.setdefault(tuple(dog_owner ),[]).append(pet)
# print(result)

# import re
#
# words = re.sub(r'[.,;:-?-!]', '', input().lower()).split()
# result = {}
# for i in words:
#     result[i] = result.get(i, 0) + 1
# res = [i for i in result if result[i] == min(result.values())]
# print(sorted(res)[0])

# Для удаления ненужных символов можно использовать конструкцию:
# import re
# words = re.sub(r'[.,;:-?-!]', '', input())
# (где
# re.sub(pattern, replacement, original_string)
# pattern: знаки препинания или шаблон выражений, которые мы хотим заменить.
# replacement: строка, которая будет заменять шаблон.)))

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# print(result)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)

# num = int(input())
# description = {1: 'One', 2: 'Two', 3: 'Three'}
# print(description.get(num, 'Unknown'))
# import random
#
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
#
# print(num1)
# print(num2)

# import random
#
# for _ in range(10):
#     print(random.randint(1, 100))
# import random
#
# num = random.random()
# print(num)

# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
#
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# import random
#
# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')

# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)

# import random
#
# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))

# import random
#
# numbers = [2, 5, 8, 9, 12]
#
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, len(numbers)))

#

# from random import choice
#
# DIGITS = '0123456789'
# LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
# UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# PUNCTUATION = '!#$%&*+-=?@^_'
#
#
# def check_user_numbers(num):  # проверка на ввод числа больше 1
#
#     if str(num).isdigit() and 1 <= int(num):
#         return int(num)
#     else:
#         print('Введите чило от 1 до n')
#         return check_user_numbers(input())
#
#
# def check_user_value_text(text):  # проверка на правильность ввода слов Да или Нет.
#
#     if text.lower() == 'да':
#         return True
#     elif text.lower() == 'нет':
#         return False
#     else:
#         print('Введите "Да" или "Нет"')
#         return check_user_value_text(input())
#
#
# pwd_quantity = check_user_numbers(input('Сколько паролей вам нужно сгенерировать? \n'))
# pwd_len = check_user_numbers(input('Какой длины должен быть пароль? \n'))
# pwd_digits = check_user_value_text(input('Включать ли в пароль цифры от 0 до 9? \n'))
# pwd_uppercase = check_user_value_text(input('Включать ли в пароль прописные буквы? \n'))
# pwd_lowercase = check_user_value_text(input('Включать ли в пароль строчные буквы? \n'))
# pwd_punctuation = check_user_value_text(input('Включать ли в пароль символы "!#$%&*+-=?@^_"? \n'))
# pwd_exceptions = check_user_value_text(input('Исключать ли неоднозначные символы "il1Lo0O"? \n'))
#
#
# def generates_a_password(password_quantity, password_len):
#     for _ in range(password_quantity):
#         chars = ''
#         for j in range(password_len):
#             if len(chars) < password_len and pwd_digits:
#                 chars += choice(DIGITS)
#             if len(chars) < password_len and pwd_lowercase:
#                 chars += choice(LOWERCASE_LETTERS)
#             if len(chars) < password_len and pwd_uppercase:
#                 chars += choice(UPPERCASE_LETTERS)
#             if len(chars) < password_len and pwd_punctuation:
#                 chars += choice(PUNCTUATION)
#             if pwd_exceptions:
#                 for c in 'il1Lo0O':
#                     chars = chars.replace(c, '')
#             elif not pwd_digits and not pwd_lowercase and not pwd_uppercase and not pwd_punctuation:
#                 print('Вы отказались от всех настроек, попробуйте снова указать настройки')
#                 return generates_a_password(pwd_quantity, pwd_len)
#         print(chars)
#
#
# generates_a_password(pwd_quantity, pwd_len)
if __name__ == '__main__':
    print('x')

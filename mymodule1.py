# s = 'abcdef'
# for c in s:
#     print(c)

# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i])

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = input()
# for c in range(len(s)):
#     if c%2==0:
#         print(s[c])
#
# s = input()
# countp=0
# counts=0
# for c in s:
#     if '+' in c:
#         countp+=1
#     if '*' in c:
#         counts+=1
# print(f'Символ + встречается {countp} раз')
# print(f'Символ * встречается {counts} раз')
#
#
# s = input()
# count=0
# for c in range(len(s)-1):
#     if s[c] == s[c+1]:
#         count+=1
# print(count)

#
# s = input()
# if s[::-1] == s[:]:
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[3])
# print(s[-3])
# print(s[-1::-1])
# print(s[1:-1])

# countmax=0
# a=0
# s= input()
# for i in s:
#     if s.count(i) >= countmax:
#         countmax = s.count(i)
#         a=i
# print(a)

# s= input()
# count=0
# if s.count('f')==1:
#     print(s.find('f'))
# elif s.count('f')>1:
#     print(s.find('f'),s.rfind('f'))
# else:
#     print('NO')

#s= input()
#print(s[0:s.find('h')]+s[s.rfind('h')+1:])

# s = input()
# for i in range(len(s)):
#     print(ord(s[i], end=' ')

# s = 'Python rocks!'
# print(s.replace('o','@'))

# s= input()
# for i in range(len(s)):
#     if i % 3!=0:
#         print(s[i], end='')

# a = [1, 2, 3, 4]
# b = [7, 8]
# a += b   # добавляем к списку a список b
# b *= 5   # повторяем список b 5 раз
#
# print(a)
# print(b)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[1] = 'ghg'     # изменяем 2 элемент (по индексу 1) списка
# print(numbers)

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
#
# print(max(numbers)+min(numbers))

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
#
# words1 = ['iq option', 'stepik', 'beegeek']
# words2 = ['iq option', 'stepik', 'beegeek']
#
# words1.append('wrcesf')
# words2.extend('wrcesf')

# print(words1)
# print(words2)

#
# a = []
# n = int(input())
# for i in range(n):
#     a.append(input())
# print(a)

# abc = 'abcdefghijklmnopqrstuvwxyz'
# s=[]
# for i in range(len(abc)):
#     s.append(abc[i]*int(i+1))
# print(s)

# a = []
# n = int(input())
# for i in range(n):
#     a.append(int(input())*int(input()))
# print(a)

# s = []
# n = int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         s.append(i)
# print(s)

# n = int(input())
# s=[]
# for i in range(n):
#     b = int(input())
#     s.append(b)
#
# del s[1::2]
# print(s)

# numbers = [0, 'sds', 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(numbers)):
#     print(i,numbers[i])


# numbers = [0, 'sds', 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in numbers:
#     print(i)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# s=[]
# for i in numbers:
#     print(s.append(i**2))
#
# n=int(input())
# s=[]
# for i in range(n):
#     a=int(input())
#     s.append(a)
# s.remove(max(s))
# s.remove(min(s))
# print(*s, sep='\n')


# n=int(input())
# s=[]
# for i in range(n):
#     a=int(input()
#     if a[i] !=a [i+1]:
#         s.append(a)
#
# print(*s, sep='\n')

# n = int(input())
# s = []
# s1 = []
# for i in range(n):
#     x = str(input())
#     s1.append(x)
#     s.append(x.lower())
# search = str(input())
# search1 = search.lower()
# for i in range(n):
#     if search1 in s[i]:
#         print(s1[i])

# s = []  # обьявляем основной список
# p = []  # обьявляем поисковый список
#
# for _ in range(int(input())):  # количество элементов основного списка
#     s.append(input())  # добавляем элементы
#
# for _ in range(int(input())):  # количество элементов поискового списка
#     p.append(input())  # добавляем элементы
#
# for i in s:  # Ищем для каждого элемента основного списка
#     n = 0  # счётчик совпадений
#     for k in p:  # сравниваем наличией элемента из списка поиска с основным
#         if k.lower() in i.lower():  # если совпадение найдено:
#             n += 1  # счётчик прибавляет значение
#     if n >= len(p):  # если счётчик совпадений равен или больше количеству элементов поискового списка, печатаем элемент из основного списка.
#         print(i)

neg = []
zero = []
poz = []
for i in range(int(input())):
    k = int(input())
    if k > 0:
        poz.append(k)
    if k < 0:
        neg.append(k)
    if k == 0:
        zero.append(k)
print(*neg, sep='\n')
print(*zero, sep='\n')
print(*poz, sep='\n')


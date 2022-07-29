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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers))
# for _ in range(int(input())):
#     print(len(set(input().lower())))
#
# a = set()
# for _ in range(int(input())):
#     c = input.lower()
#     for j in c:
#         a.add(j)
# print(len(a))

# s = set()
# for i in input():
#     s.add(i)
#     if i in set:
#         print('YES')
#     else:
#         print('NO')

# a =list(map(int,input().split()))
# a=set(a)
# b =list(map(int,input().split()))
# b=set(b)
# print(len(a & b))

# s1 = set(input().split())
# s2 = set(input().split())
# print(len(s1 & s2))

# s1 = set(input().split())
# s2 = set(input().split())
# s3=set(sorted(s1 & s2))
# print(*s3)

# a = set(input())
# b = set(input())
# if a.isdisjoint(b):
#     print('NO')
# else:
#     print('YES')

# a, b, c = (set(int(i) for i in input().split()) for i in range(3))
#
# print(*sorted((a&b)-c, reverse=True))


# a, b, c = (set(int(i) for i in input().split()) for i in range(3))
#
# print(*sorted(a|b|c)-(a&b&c))
#
# set1, set2, set3 = [set([int(i) for i in input().split()]) for k in range(3)]
# print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

# chars = {c for c in 'abcdefg'}
# print(chars)

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# print({int(i) for i in items})

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# print(*sorted({i[0].lower() for i in words}))

import re
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# stroka = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
# spisok = stroka.lower().split()
# myset = set(spisok)
# print(*sorted(myset))

# re.sub(pattern, replacement, original_string)
# pattern: знаки препинания или шаблон выражений, которые мы хотим заменить.
# replacement: строка, которая будет заменять шаблон.)))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# import re
# stroka = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
# spisok = stroka.lower().split()
# myset = {i for i in spisok if len(i) <4}
# print(*sorted(myset))

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

s={i.lower() for i in files if i.lower().endswith('png')}
print(*sorted(s))


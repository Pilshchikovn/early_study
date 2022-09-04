# a, b = map(int, input().split())
# print(a % b == 0)

# a =float(input())
# print((0>=a<=2) or (10>=a<=20))

# a = str(input())
# b = str(input())
# s= (a*2)+" "+(b*3)
# print(s)
# a = str(input())
# print("Строка: " + str(a) + ". Длина:" + str(len(a)))

# a,b = input().split()
# print(a in b,a == b,a > b,a < b)

# a = map(str, input.split())

# a,b = map(str,input().split())
# x = len(a)
# print(b[:x:])

# a = input().split()
# print(a.replace(' ','\',1).replace(' ', '\''))
# a = input()
# b = input()
# c = int(input())
# d = float(input())
# book =[a,b.replace('Булгаков','Пушкин'),d*2]
# print(book)
#
# a = list(map(int,input().split()))
# print(sorted(a, reverse =True))

# list =[1,2,3]
# print(*list)

# rivers = ['Ob','ddg','fhf']
# rivers.sort()
# rivers.pop(2)
# print(rivers)

# a = [5.4, 6.7, 10.4]
# b = list(map(int, input().split()))
# a.append(b)
# print(a)

# a = list(input().split())
# b = list(input().split())
# c = list(input().split())
# print(a[-1],b[-1],c[-1])

# a, b = map(float, input().split())

# m, n = map(int, input().split())
# if m % n == 0:
#     print(int(m // n))
# else:
#     print(f"{m} на {n} нацело не делится")

# a,b,c = map(int, input().split())
#
#
# a,b,c = map(int, input().split())
# if c**2==(a**2)+(b**2):
#     print('ДА')
# else:
#     print('НЕТ')
#
# a = int(input())
# if a % 10 == 7:
#     print('ДА')
# else:
#     print('НЕТ')
#
# a, b, c, d=map(int,input().split())
# if b>d+1 and a>c+1 or b>c+1 and a>d+1:
#     print("ДА")
# else:
#     print("НЕТ")
#
# k = int(input())
# a = 1 <= k <= 365
# if a%7==0:
#     print("понедельник")
# elif  a%7==1 :
#     print("вторник")
# elif  a%7==2:
#     print("среда")
# elif  a%7==3:
#     print("четверг")
# elif  a%7==4:
#     print("пятница")
# elif  a%7==5:
#     print("суббота")
# elif  a%7==6:
#     print("воскресенье")

# temp = input().split(' ')
# lst = [abs(float(x)) for x in temp]
# print(lst)
#
# a = input()
# lst = [abs(float(x)) for x in a.split()]
# print(lst)
#
# a = input()
# lst = [int(x) for x in a]
# print(lst)

# a = input()
# s = [ i for i in a.split() if len(i) > 5]
# print(*s)

n = int(input())
a = [b for b in range(1, n+1) if n % b == 0]
print(*a)

N = int(input())
[print(*[i] * N) for i in range(N)]

lst = [float(x) for i, x in enumerate(input().split()) if i % 2 == 0]
print(*lst)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
lst = [a[i]+b[i] for i in range(len(a))]
print(*lst)

n = input().split()
lst = [[n[i], int(n[i + 1])] for i in range(0, len(n), 2)]
print(lst)
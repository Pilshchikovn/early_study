# a = int(input())
# if a % 10 == 7:
#     print('ДА')
# else:
#     print('НЕТ')
#
#
# a, b, c, d = map(int, input().split())
# if b > d + 1 and a > c + 1 or b > c + 1 and a > d + 1:
#     print("ДА")
# else:
#     print("НЕТ")

# a, b, c = map(int, input().split())
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)

# a = float(input())
# if a <= 60:
#     print('легкий вес')
# elif a <= 64:
#     print('первый полусредний вес')
# elifa <= 69:
#     print('полусредний вес')
# else:
#     print('остальные')

# d = int(input())-1
# dname = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# if d==0:
#     print (dname[0])
# elif d==1:
#     print (dname[1])
# elif d==2:
#     print (dname[2])
# elif d==3:
#     print (dname[3])
# elif d==4:
#     print (dname[4])
# elif d==5:
#     print (dname[5])
# elif d==6:
#     print (dname[6])
# else :
#     print('неверный номер')

a = int(input())
t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= a <= 12:
    a = t[a - 1]
    print(a)
else:
    print("Вообще не месяц")
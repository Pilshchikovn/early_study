# n = [1, 2, 3]
# x = ''.join(str(i) for i in n)
# print(x, end=' ')  #  123

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# s = input().split()
# print(* s, sep="\n")

# print('\n'.join(input().split()))
#
# s = input().split()
# for i in (s):
#     print(i[0], end=".")
#
# s = input().split()
# print(s[0][0]+'.'+s[1][0]+'.'+s[2][0]+'.')
#
# s = input().split()
# for i in s:
#     print(int(i)*'+', sep='\n')
#
# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

# print(*list(input()), sep=input())
#
# l=input().split()
# c=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[j]==l[i]:
#             c+=1
# print(c)

# names = ['Gvido', 'Roman' , 'Timur']
# item = names.pop(1)
# print(item)
# print(names)
#
# numbers = [8, 9, 10, 11]
# numbers[1]=17
# numbers.extend([4,5,6])
# del numbers[0]
# numbers*=2
# numbers.insert(3,25)
# print(numbers)


# a = list(map(int, input().split()))
# b = a.index(min(a))
# c = a.index(max(a))
# a[b], a[c] = a[c], a[b]
# print(*a)

# s = input().lower().split()
# print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")

#
# n = input().split()   #считываем данные
# for i in range(len(n)):     #запускаем цикл
#     n[i] = int(n[i])        #преобразуем строковые данные в цифровые
# n.sort()              #сортируем список
# print(*n)             #выводим на печать 1-ую строку
# n.sort(reverse=True)  #переворачиваем отсортированный список
# print(*n)             #выводим на печать 2-ую строку

# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())

# zeros = []
# for i in range(10):
#     zeros.append(0)
#
# numbers = [i for i in range(10)]
#
# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)

# print(*[i**2 for i in range(1,int(input())+1)], sep = '\n')

# print(*((i for i in input().split() if i.isdigit()), sep='\n')

# print(*[int(i)**2 for i in input().split() if int(i)%2==0 and int(i)**2%10!=4])

# print([i for i in range(2,int(input())) if i%2==0])

# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# result = [lst1[i] + lst2[i] for i in range(len(lst1))]
# print(*result)

# s = list(str(input()).split())
# x = '+'.join(s)
# y=[int(i) for i in s]
# print(f'{x}={sum(y)})

# print(*[i[1:] +i[0] +'ки' for i in list(str(input()).split())])





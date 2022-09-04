# lst = list(map(str, input().split()))
# i = 0
# ans = 'ДА'
# while i < len(lst):
#     if len(lst[i]) < 6:
#         ans = 'НЕТ'
#         break
#     else:
#         i += 1
# print(ans)
#
#
# stud = list(map(str, input().split()))
# i = 0
# studLenList = len(stud) - 1
# while studLenList >= 0:
#     if str.lower(stud[i][0]) == str.lower(stud[i][-1]):
#         print("ДА")
#         break
#     i += 1
#     studLenList -= 1
# else:
#     print("НЕТ")
# n = int(input())
# a = 0
# while n < 100:
#     a += 1
#     if a <= n < 100:
#         if a % 3 == 0 and a % 5 == 0:
#             print(a, end=' ')
#     else:
#         break
# else:
#     print('слишком большое значение n')

# n = int(input())
# i = 1
# while True:
#     if i**2 > n:
#         print(i)
#         break
#     i+=1

# x = range(0,11)
# for i in x:
#     print(i, end = ' ')


# stud = list(map(int, input().split()))
# for i in stud:
#     if i%2 !=0:
#         print(sum(i))

# lst = list(map(str, input().split()))
# for i in lst:
#     print(len(i), end = ' ')

# n = int(input())
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)
#
# x = int(input())
# if x//x ==0 and x//1 == 0:
#     print('ДА')
# else:
#     print('НЕТ')

n = int(input())
s=0
for i in range(n-1,0,-1):
    if i %3 == 0 or i %5 == 0:
        s +=i
print(s)

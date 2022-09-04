# # a = float(input())
# # b = float(input())
# # d = a if a > b else b
# # print(d)
# #
# # a =int(input())
# # msg = "кратно 3" if a%3==0 else "не кратно 3"
# # print(msg)
# #
# #
# # a =str(input().lower())
# # a.lower()
# # msg = "палиндром" if (a==a[::-1]) else "не палиндром"
# # print(msg)
# #
# # a = int(input())
# # rez = 0 if a + 1 == 60 else a + 1
# # print(rez)
#
# n,m = map(int,input().split())
#
# n, m = map(int, input().split())
# while n <= m:
#         print(n**2, end=' ')
#         n += 1
#
# n, m = map(int, input().split())
# l=[]
# while n<=m:
#     l.append(n**2)
#     n=n+1
# print(*l)
#
#
# x=float(input())
# a = []
# b=1
# while b<10:
#     b=b+1
#     a.append(round(b*x,1))
# print(*a)
#
# sum=0
# k=1
# n=int(input())
# while k<=n:
#     sum=sum+1/k
#     k+=1
# print(round(sum,3))

# summ = 0
# k = ""
# while k != 0:
#     k = int(input())
#     summ = summ + k
# print (summ)
#

# a = str(input())
# while "--" in a:
#     a = a.replace("--", "-")
# print(a)
#
# n = list(map(int,input()))
# i = 0
# s = 1
# while i != len(n):
#     s = s * n[i]
#     i += 1
# print(s)
#
# fib = [1, 1]
# a = int(input())
# while len(fib) < a:
#     fib.append(fib[-1] + fib[-2])
#
# print(*fib)
#
# n = int(input())
# res = 1
# while n > 3:
#     res *= 2
#     n -= 3
# print(res)
#
# n = int(input())
# dep = 1000.00
# while n > 0:
#     n -= 1
#     dep *= 1.05
# print(round(dep, 2))

# n,m = map(int, input().split())
# sum = []
# while n < m:
#     sum.append(n)
#     n +=1
# print(*sum[1::2])


# x = 100
# while(x <= 999):
#     if(x%47 == 43 and x%3 == 0):
#         print(x, end=" ")
#     x += 1

lst = list(map(str, input().split()))
i = 0
ans = 'ДА'
while i < len(lst):
    if len(lst[i]) < 6:
        ans = 'НЕТ'
        break
    else:
        i += 1
print(ans)


stud = list(map(str, input().split()))
i = 0
studLenList = len(stud) - 1
while studLenList >= 0:
    if str.lower(stud[i][0]) == str.lower(stud[i][-1]):
        print("ДА")
        break
    i += 1
    studLenList -= 1
else:
    print("НЕТ")
n = int(input())
a = 0
while n < 100:
    a += 1
    if a <= n < 100:
        if a % 3 == 0 and a % 5 == 0:
            print(a, end=' ')
    else:
        break
else:
    print('слишком большое значение n')


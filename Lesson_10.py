# n=int(input())
# for i in range(n):
#     r=[]
#     for j in range(n-1):
#         r.append(1)
#     r.append(5)
#     print(*r)
#
# n = int(input())
# for i in range(n):
#     for j in range(n-1):
#         print(1, end= " ")
#     print(5)
#
# n = int(input())
# x = [[1] * n for i in range(n)]
# for i in range(n):
#     x[i][-1] = 5
#     print(*x[i])
#
# n = int(input())
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# for f, i in enumerate(lst_in):
#     lst_in[f] = (i.split())
#     lst_in[f] = "-".join(lst_in[f])
#
# print(*lst_in)